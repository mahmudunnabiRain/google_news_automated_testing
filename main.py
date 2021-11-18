# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print("run 'python -m unittest' to start test")  # Press Ctrl+F8 to toggle the breakpoint.


def test_codes():
    from selenium import webdriver
    driver = webdriver.Chrome('./drivers/chromedriver')
    driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
