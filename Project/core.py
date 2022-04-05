import csv
import time

import pandas as pd
import config


class PlaceClass:
    def __init__(self, data_location):
        self.start_time = time.time()
        self.data_location = data_location
        self.data = self.read_data()
        self.data["blank"] = 0

    def read_data(self):
        df = pd.read_csv(self.data_location)
        df["ts"] = pd.to_datetime(df["ts"], utc=True, unit="ms")
        df["color"] = df["color"].map(config.color_map)
        return df

    def pivot(
        self, df, vals=["ts"], idx=["user"], cols=["color"], rename_dict={}, agg="count"
    ):
        result = pd.pivot_table(df, values=vals, columns=cols, index=idx, aggfunc=agg)
        result.rename(columns=rename_dict, inplace=True)
        return result

    def generate_summaries(self, year, print_it=True):
        users = self.pivot(self.data, rename_dict={"color": "tiles_placed"})
        px = self.pivot(
            self.data,
            idx=["x_coordinate", "y_coordinate"],
            rename_dict={"color": "tiles_placed"},
        )
        clr = self.pivot(self.data, idx=["color"], cols=["blank"])
        ts = self.pivot(self.data, idx=["ts"], cols=["color"], vals="user")

        for key, ea in {"users": users, "px": px, "clr": clr, "ts": ts}.items():
            ea["tot"] = ea[list(ea.columns)].sum(axis=1)
            ea.sort_values(by=["tot"], ascending=False, inplace=True)
            ea.to_csv(f"Results/{key}_{str(year)}.csv")
        if print_it:
            self.printer()

    def printer(self):
        print(self.data.head())
        print(self.data.dtypes)
        print(time.time() - self.start_time)


def main():
    place_2017 = PlaceClass("Data/2017/tile_placements.csv")

    place_2017.generate_summaries(year=2017, print_it=True)

    return None


if __name__ == "__main__":
    """[summary]"""
    main()
