import conducto as co


def build_and_test() -> co.Serial:
    image = co.Image(copy_dir="./code")
    with co.Serial(image=image, stop_on_error=False) as pipeline:
        with co.Parallel(name="Trade") as first_trading:
            first_trading['US'] = co.Exec("python3 first_stock_trading.py")
            first_trading['CHINA'] = co.Exec("python3 second_stock_trading.py")
        with co.Parallel(name="TopK") as second_trading:
            second_trading['US'] = co.Exec("python3 first_topK_stock_pipeline.py")
            second_trading['CHINA'] = co.Exec("python3 second_topK_stock_pipeline.py")

    return pipeline

if __name__ == "__main__":

    co.main(default=build_and_test)
