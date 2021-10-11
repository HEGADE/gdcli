import webbrowser


def open_browser(url: str)->None:
    if type(url) is str:
        try:
            webbrowser.open(url)

        except Exception as e:
            pass
    else:
        print("Function call with invalid arguments")


if __name__ == "__main__":
    open_browser(None)
