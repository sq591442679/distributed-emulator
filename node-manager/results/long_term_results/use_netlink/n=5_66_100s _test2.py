import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

data = {
    "n=0": [
        [
        {
            "time": " 1.0",
            "now drop rate": " 9.2%"
        },
        {
            "time": " 2.0",
            "now drop rate": " 5.3%"
        },
        {
            "time": " 3.0",
            "now drop rate": " 4.1%"
        },
        {
            "time": " 4.0",
            "now drop rate": " 3.4%"
        },
        {
            "time": " 5.0",
            "now drop rate": " 3.1%"
        },
        {
            "time": " 6.0",
            "now drop rate": " 2.8%"
        },
        {
            "time": " 7.0",
            "now drop rate": " 2.6%"
        },
        {
            "time": " 8.0",
            "now drop rate": " 2.5%"
        },
        {
            "time": " 9.0",
            "now drop rate": " 2.3%"
        },
        {
            "time": " 10.0",
            "now drop rate": " 2.2%"
        },
        {
            "time": " 11.0",
            "now drop rate": " 2.2%"
        },
        {
            "time": " 12.1",
            "now drop rate": " 2.1%"
        },
        {
            "time": " 13.1",
            "now drop rate": " 2.0%"
        },
        {
            "time": " 14.1",
            "now drop rate": " 2.0%"
        },
        {
            "time": " 15.1",
            "now drop rate": " 2.0%"
        },
        {
            "time": " 16.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 17.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 18.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 19.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 20.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 21.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 22.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 27.8",
            "now drop rate": " 19.5%"
        },
        {
            "time": " 28.8",
            "now drop rate": " 20.5%"
        },
        {
            "time": " 29.8",
            "now drop rate": " 19.9%"
        },
        {
            "time": " 30.8",
            "now drop rate": " 19.3%"
        },
        {
            "time": " 31.8",
            "now drop rate": " 18.7%"
        },
        {
            "time": " 32.8",
            "now drop rate": " 18.2%"
        },
        {
            "time": " 33.8",
            "now drop rate": " 17.8%"
        },
        {
            "time": " 34.9",
            "now drop rate": " 17.3%"
        },
        {
            "time": " 35.9",
            "now drop rate": " 16.9%"
        },
        {
            "time": " 36.9",
            "now drop rate": " 16.5%"
        },
        {
            "time": " 37.9",
            "now drop rate": " 16.1%"
        },
        {
            "time": " 38.9",
            "now drop rate": " 15.7%"
        },
        {
            "time": " 39.9",
            "now drop rate": " 15.3%"
        },
        {
            "time": " 40.9",
            "now drop rate": " 14.9%"
        },
        {
            "time": " 41.9",
            "now drop rate": " 14.6%"
        },
        {
            "time": " 42.9",
            "now drop rate": " 14.3%"
        },
        {
            "time": " 43.9",
            "now drop rate": " 14.0%"
        },
        {
            "time": " 44.9",
            "now drop rate": " 13.7%"
        },
        {
            "time": " 45.9",
            "now drop rate": " 13.4%"
        },
        {
            "time": " 46.9",
            "now drop rate": " 13.2%"
        },
        {
            "time": " 47.9",
            "now drop rate": " 12.9%"
        },
        {
            "time": " 48.9",
            "now drop rate": " 12.7%"
        },
        {
            "time": " 49.9",
            "now drop rate": " 12.5%"
        },
        {
            "time": " 50.9",
            "now drop rate": " 12.3%"
        },
        {
            "time": " 51.9",
            "now drop rate": " 12.0%"
        },
        {
            "time": " 52.9",
            "now drop rate": " 11.8%"
        },
        {
            "time": " 53.9",
            "now drop rate": " 11.6%"
        },
        {
            "time": " 54.9",
            "now drop rate": " 11.5%"
        },
        {
            "time": " 55.9",
            "now drop rate": " 11.3%"
        },
        {
            "time": " 56.9",
            "now drop rate": " 11.1%"
        },
        {
            "time": " 57.9",
            "now drop rate": " 10.9%"
        },
        {
            "time": " 58.9",
            "now drop rate": " 10.8%"
        },
        {
            "time": " 59.9",
            "now drop rate": " 10.6%"
        },
        {
            "time": " 61.0",
            "now drop rate": " 10.5%"
        },
        {
            "time": " 62.0",
            "now drop rate": " 10.3%"
        },
        {
            "time": " 63.0",
            "now drop rate": " 10.2%"
        },
        {
            "time": " 64.0",
            "now drop rate": " 10.0%"
        },
        {
            "time": " 65.0",
            "now drop rate": " 9.9%"
        },
        {
            "time": " 66.0",
            "now drop rate": " 9.8%"
        },
        {
            "time": " 67.0",
            "now drop rate": " 9.6%"
        },
        {
            "time": " 68.0",
            "now drop rate": " 9.5%"
        },
        {
            "time": " 69.0",
            "now drop rate": " 9.4%"
        },
        {
            "time": " 70.0",
            "now drop rate": " 9.3%"
        },
        {
            "time": " 71.0",
            "now drop rate": " 9.2%"
        },
        {
            "time": " 72.0",
            "now drop rate": " 9.1%"
        },
        {
            "time": " 73.0",
            "now drop rate": " 9.0%"
        },
        {
            "time": " 74.0",
            "now drop rate": " 8.9%"
        },
        {
            "time": " 75.0",
            "now drop rate": " 8.8%"
        },
        {
            "time": " 76.0",
            "now drop rate": " 8.7%"
        },
        {
            "time": " 77.0",
            "now drop rate": " 8.6%"
        },
        {
            "time": " 78.0",
            "now drop rate": " 8.5%"
        },
        {
            "time": " 79.1",
            "now drop rate": " 8.6%"
        },
        {
            "time": " 80.1",
            "now drop rate": " 8.4%"
        },
        {
            "time": " 81.1",
            "now drop rate": " 8.3%"
        },
        {
            "time": " 82.1",
            "now drop rate": " 8.3%"
        },
        {
            "time": " 83.1",
            "now drop rate": " 8.2%"
        },
        {
            "time": " 84.1",
            "now drop rate": " 8.1%"
        },
        {
            "time": " 85.1",
            "now drop rate": " 8.0%"
        },
        {
            "time": " 86.1",
            "now drop rate": " 7.9%"
        },
        {
            "time": " 87.1",
            "now drop rate": " 7.8%"
        },
        {
            "time": " 88.1",
            "now drop rate": " 7.8%"
        },
        {
            "time": " 89.1",
            "now drop rate": " 7.7%"
        },
        {
            "time": " 90.2",
            "now drop rate": " 7.6%"
        },
        {
            "time": " 91.2",
            "now drop rate": " 7.5%"
        },
        {
            "time": " 92.2",
            "now drop rate": " 7.5%"
        },
        {
            "time": " 93.2",
            "now drop rate": " 7.4%"
        },
        {
            "time": " 94.2",
            "now drop rate": " 7.3%"
        },
        {
            "time": " 95.2",
            "now drop rate": " 7.3%"
        },
        {
            "time": " 96.2",
            "now drop rate": " 7.2%"
        },
        {
            "time": " 97.2",
            "now drop rate": " 7.2%"
        },
        {
            "time": " 98.2",
            "now drop rate": " 7.1%"
        },
        {
            "time": " 99.2",
            "now drop rate": " 7.0%"
        },
        {
            "drop rate": " 6.9%",
            "delay": " 104.3"
        }
        ],
        [
        {
            "time": " 1.0",
            "now drop rate": " 8.7%"
        },
        {
            "time": " 2.0",
            "now drop rate": " 5.1%"
        },
        {
            "time": " 3.0",
            "now drop rate": " 4.0%"
        },
        {
            "time": " 4.0",
            "now drop rate": " 3.4%"
        },
        {
            "time": " 5.0",
            "now drop rate": " 3.1%"
        },
        {
            "time": " 6.0",
            "now drop rate": " 2.9%"
        },
        {
            "time": " 7.1",
            "now drop rate": " 2.7%"
        },
        {
            "time": " 8.1",
            "now drop rate": " 2.5%"
        },
        {
            "time": " 9.1",
            "now drop rate": " 2.4%"
        },
        {
            "time": " 10.1",
            "now drop rate": " 2.3%"
        },
        {
            "time": " 11.1",
            "now drop rate": " 2.2%"
        },
        {
            "time": " 12.1",
            "now drop rate": " 2.1%"
        },
        {
            "time": " 13.1",
            "now drop rate": " 2.1%"
        },
        {
            "time": " 14.1",
            "now drop rate": " 2.1%"
        },
        {
            "time": " 15.1",
            "now drop rate": " 2.0%"
        },
        {
            "time": " 16.1",
            "now drop rate": " 2.0%"
        },
        {
            "time": " 17.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 18.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 19.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 20.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 21.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 22.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 27.7",
            "now drop rate": " 19.6%"
        },
        {
            "time": " 28.7",
            "now drop rate": " 17.8%"
        },
        {
            "time": " 29.7",
            "now drop rate": " 17.3%"
        },
        {
            "time": " 30.7",
            "now drop rate": " 16.8%"
        },
        {
            "time": " 31.7",
            "now drop rate": " 16.3%"
        },
        {
            "time": " 32.7",
            "now drop rate": " 15.9%"
        },
        {
            "time": " 34.4",
            "now drop rate": " 18.0%"
        },
        {
            "time": " 35.4",
            "now drop rate": " 17.4%"
        },
        {
            "time": " 36.4",
            "now drop rate": " 16.9%"
        },
        {
            "time": " 37.4",
            "now drop rate": " 16.5%"
        },
        {
            "time": " 38.4",
            "now drop rate": " 16.1%"
        },
        {
            "time": " 39.4",
            "now drop rate": " 15.8%"
        },
        {
            "time": " 40.4",
            "now drop rate": " 15.3%"
        },
        {
            "time": " 41.4",
            "now drop rate": " 15.0%"
        },
        {
            "time": " 42.4",
            "now drop rate": " 14.7%"
        },
        {
            "time": " 43.4",
            "now drop rate": " 14.4%"
        },
        {
            "time": " 44.4",
            "now drop rate": " 14.1%"
        },
        {
            "time": " 45.5",
            "now drop rate": " 13.8%"
        },
        {
            "time": " 46.5",
            "now drop rate": " 13.6%"
        },
        {
            "time": " 47.5",
            "now drop rate": " 13.3%"
        },
        {
            "time": " 48.5",
            "now drop rate": " 13.1%"
        },
        {
            "time": " 49.5",
            "now drop rate": " 12.8%"
        },
        {
            "time": " 50.5",
            "now drop rate": " 12.6%"
        },
        {
            "time": " 51.5",
            "now drop rate": " 12.4%"
        },
        {
            "time": " 52.5",
            "now drop rate": " 12.2%"
        },
        {
            "time": " 53.5",
            "now drop rate": " 12.0%"
        },
        {
            "time": " 54.5",
            "now drop rate": " 11.8%"
        },
        {
            "time": " 55.5",
            "now drop rate": " 11.6%"
        },
        {
            "time": " 56.5",
            "now drop rate": " 11.4%"
        },
        {
            "time": " 57.5",
            "now drop rate": " 11.2%"
        },
        {
            "time": " 58.5",
            "now drop rate": " 11.1%"
        },
        {
            "time": " 59.5",
            "now drop rate": " 10.9%"
        },
        {
            "time": " 60.5",
            "now drop rate": " 10.8%"
        },
        {
            "time": " 61.5",
            "now drop rate": " 10.7%"
        },
        {
            "time": " 62.5",
            "now drop rate": " 10.5%"
        },
        {
            "time": " 63.5",
            "now drop rate": " 10.4%"
        },
        {
            "time": " 64.5",
            "now drop rate": " 10.2%"
        },
        {
            "time": " 65.6",
            "now drop rate": " 10.1%"
        },
        {
            "time": " 66.6",
            "now drop rate": " 10.0%"
        },
        {
            "time": " 67.6",
            "now drop rate": " 9.9%"
        },
        {
            "time": " 68.6",
            "now drop rate": " 9.8%"
        },
        {
            "time": " 69.6",
            "now drop rate": " 9.6%"
        },
        {
            "time": " 70.6",
            "now drop rate": " 9.6%"
        },
        {
            "time": " 71.6",
            "now drop rate": " 9.4%"
        },
        {
            "time": " 72.6",
            "now drop rate": " 9.3%"
        },
        {
            "time": " 73.6",
            "now drop rate": " 9.2%"
        },
        {
            "time": " 74.6",
            "now drop rate": " 9.1%"
        },
        {
            "time": " 75.6",
            "now drop rate": " 9.0%"
        },
        {
            "time": " 76.6",
            "now drop rate": " 8.9%"
        },
        {
            "time": " 77.6",
            "now drop rate": " 8.8%"
        },
        {
            "time": " 78.6",
            "now drop rate": " 8.7%"
        },
        {
            "time": " 79.6",
            "now drop rate": " 8.7%"
        },
        {
            "time": " 80.6",
            "now drop rate": " 8.6%"
        },
        {
            "time": " 81.6",
            "now drop rate": " 8.5%"
        },
        {
            "time": " 82.6",
            "now drop rate": " 8.4%"
        },
        {
            "time": " 83.6",
            "now drop rate": " 8.3%"
        },
        {
            "time": " 84.6",
            "now drop rate": " 8.3%"
        },
        {
            "time": " 85.6",
            "now drop rate": " 8.2%"
        },
        {
            "time": " 86.6",
            "now drop rate": " 8.1%"
        },
        {
            "time": " 87.7",
            "now drop rate": " 8.0%"
        },
        {
            "time": " 88.7",
            "now drop rate": " 7.9%"
        },
        {
            "time": " 89.7",
            "now drop rate": " 7.9%"
        },
        {
            "time": " 90.7",
            "now drop rate": " 7.8%"
        },
        {
            "time": " 91.7",
            "now drop rate": " 7.7%"
        },
        {
            "time": " 92.7",
            "now drop rate": " 7.6%"
        },
        {
            "time": " 93.7",
            "now drop rate": " 7.6%"
        },
        {
            "time": " 94.7",
            "now drop rate": " 7.5%"
        },
        {
            "time": " 95.7",
            "now drop rate": " 7.4%"
        },
        {
            "time": " 96.7",
            "now drop rate": " 7.4%"
        },
        {
            "time": " 97.7",
            "now drop rate": " 7.3%"
        },
        {
            "time": " 98.7",
            "now drop rate": " 7.3%"
        },
        {
            "time": " 99.7",
            "now drop rate": " 7.2%"
        },
        {
            "drop rate": " 7.1%",
            "delay": " 107.4"
        }
        ],
        [
        {
            "time": " 1.0",
            "now drop rate": " 7.0%"
        },
        {
            "time": " 2.0",
            "now drop rate": " 4.2%"
        },
        {
            "time": " 3.0",
            "now drop rate": " 3.3%"
        },
        {
            "time": " 4.0",
            "now drop rate": " 2.9%"
        },
        {
            "time": " 5.0",
            "now drop rate": " 2.6%"
        },
        {
            "time": " 6.0",
            "now drop rate": " 2.4%"
        },
        {
            "time": " 7.0",
            "now drop rate": " 2.2%"
        },
        {
            "time": " 8.0",
            "now drop rate": " 2.1%"
        },
        {
            "time": " 9.0",
            "now drop rate": " 2.0%"
        },
        {
            "time": " 10.0",
            "now drop rate": " 2.0%"
        },
        {
            "time": " 11.0",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 12.0",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 13.0",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 14.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 15.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 16.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 17.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 18.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 19.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 20.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 21.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 22.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 23.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 24.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 25.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 28.1",
            "now drop rate": " 8.9%"
        },
        {
            "time": " 29.1",
            "now drop rate": " 6.0%"
        },
        {
            "time": " 30.1",
            "now drop rate": " 5.9%"
        },
        {
            "time": " 31.1",
            "now drop rate": " 5.7%"
        },
        {
            "time": " 32.1",
            "now drop rate": " 5.6%"
        },
        {
            "time": " 33.1",
            "now drop rate": " 5.5%"
        },
        {
            "time": " 34.1",
            "now drop rate": " 5.5%"
        },
        {
            "time": " 39.3",
            "now drop rate": " 17.5%"
        },
        {
            "time": " 40.3",
            "now drop rate": " 15.6%"
        },
        {
            "time": " 41.3",
            "now drop rate": " 15.2%"
        },
        {
            "time": " 42.3",
            "now drop rate": " 14.9%"
        },
        {
            "time": " 43.3",
            "now drop rate": " 14.6%"
        },
        {
            "time": " 44.4",
            "now drop rate": " 14.3%"
        },
        {
            "time": " 45.4",
            "now drop rate": " 14.0%"
        },
        {
            "time": " 46.4",
            "now drop rate": " 13.8%"
        },
        {
            "time": " 47.4",
            "now drop rate": " 13.5%"
        },
        {
            "time": " 48.4",
            "now drop rate": " 13.2%"
        },
        {
            "time": " 49.4",
            "now drop rate": " 13.0%"
        },
        {
            "time": " 50.4",
            "now drop rate": " 12.8%"
        },
        {
            "time": " 51.4",
            "now drop rate": " 12.5%"
        },
        {
            "time": " 52.4",
            "now drop rate": " 12.3%"
        },
        {
            "time": " 53.4",
            "now drop rate": " 12.1%"
        },
        {
            "time": " 54.4",
            "now drop rate": " 11.9%"
        },
        {
            "time": " 55.4",
            "now drop rate": " 11.8%"
        },
        {
            "time": " 56.4",
            "now drop rate": " 11.6%"
        },
        {
            "time": " 57.4",
            "now drop rate": " 11.4%"
        },
        {
            "time": " 58.4",
            "now drop rate": " 11.2%"
        },
        {
            "time": " 59.4",
            "now drop rate": " 11.1%"
        },
        {
            "time": " 60.4",
            "now drop rate": " 10.9%"
        },
        {
            "time": " 61.4",
            "now drop rate": " 10.8%"
        },
        {
            "time": " 62.5",
            "now drop rate": " 10.6%"
        },
        {
            "time": " 63.5",
            "now drop rate": " 10.5%"
        },
        {
            "time": " 64.5",
            "now drop rate": " 10.3%"
        },
        {
            "time": " 65.5",
            "now drop rate": " 10.2%"
        },
        {
            "time": " 66.5",
            "now drop rate": " 10.0%"
        },
        {
            "time": " 67.5",
            "now drop rate": " 9.9%"
        },
        {
            "time": " 68.5",
            "now drop rate": " 9.8%"
        },
        {
            "time": " 69.5",
            "now drop rate": " 9.7%"
        },
        {
            "time": " 70.5",
            "now drop rate": " 9.6%"
        },
        {
            "time": " 71.5",
            "now drop rate": " 9.5%"
        },
        {
            "time": " 72.5",
            "now drop rate": " 9.4%"
        },
        {
            "time": " 73.5",
            "now drop rate": " 9.3%"
        },
        {
            "time": " 74.5",
            "now drop rate": " 9.2%"
        },
        {
            "time": " 75.5",
            "now drop rate": " 9.0%"
        },
        {
            "time": " 76.5",
            "now drop rate": " 8.9%"
        },
        {
            "time": " 77.5",
            "now drop rate": " 8.8%"
        },
        {
            "time": " 78.5",
            "now drop rate": " 8.7%"
        },
        {
            "time": " 79.5",
            "now drop rate": " 8.7%"
        },
        {
            "time": " 80.5",
            "now drop rate": " 8.6%"
        },
        {
            "time": " 81.5",
            "now drop rate": " 8.5%"
        },
        {
            "time": " 82.5",
            "now drop rate": " 8.4%"
        },
        {
            "time": " 83.5",
            "now drop rate": " 8.4%"
        },
        {
            "time": " 84.5",
            "now drop rate": " 8.3%"
        },
        {
            "time": " 85.6",
            "now drop rate": " 8.2%"
        },
        {
            "time": " 86.6",
            "now drop rate": " 8.1%"
        },
        {
            "time": " 87.6",
            "now drop rate": " 8.0%"
        },
        {
            "time": " 88.6",
            "now drop rate": " 7.9%"
        },
        {
            "time": " 89.6",
            "now drop rate": " 7.9%"
        },
        {
            "time": " 90.6",
            "now drop rate": " 7.8%"
        },
        {
            "time": " 91.6",
            "now drop rate": " 7.7%"
        },
        {
            "time": " 92.6",
            "now drop rate": " 7.6%"
        },
        {
            "time": " 93.6",
            "now drop rate": " 7.6%"
        },
        {
            "time": " 94.6",
            "now drop rate": " 7.5%"
        },
        {
            "time": " 95.6",
            "now drop rate": " 7.5%"
        },
        {
            "time": " 96.6",
            "now drop rate": " 7.4%"
        },
        {
            "time": " 97.6",
            "now drop rate": " 7.3%"
        },
        {
            "time": " 98.6",
            "now drop rate": " 7.3%"
        },
        {
            "time": " 99.6",
            "now drop rate": " 7.2%"
        },
        {
            "drop rate": " 7.1%",
            "delay": " 110.8"
        }
        ],
        [
        {
            "time": " 1.0",
            "now drop rate": " 10.8%"
        },
        {
            "time": " 2.0",
            "now drop rate": " 6.2%"
        },
        {
            "time": " 3.0",
            "now drop rate": " 4.7%"
        },
        {
            "time": " 4.0",
            "now drop rate": " 3.9%"
        },
        {
            "time": " 5.0",
            "now drop rate": " 3.5%"
        },
        {
            "time": " 6.0",
            "now drop rate": " 3.1%"
        },
        {
            "time": " 7.0",
            "now drop rate": " 3.1%"
        },
        {
            "time": " 8.1",
            "now drop rate": " 2.9%"
        },
        {
            "time": " 9.1",
            "now drop rate": " 2.8%"
        },
        {
            "time": " 10.1",
            "now drop rate": " 2.7%"
        },
        {
            "time": " 11.1",
            "now drop rate": " 2.6%"
        },
        {
            "time": " 12.1",
            "now drop rate": " 2.5%"
        },
        {
            "time": " 13.1",
            "now drop rate": " 2.5%"
        },
        {
            "time": " 14.1",
            "now drop rate": " 2.4%"
        },
        {
            "time": " 15.1",
            "now drop rate": " 2.3%"
        },
        {
            "time": " 16.1",
            "now drop rate": " 2.3%"
        },
        {
            "time": " 17.1",
            "now drop rate": " 2.3%"
        },
        {
            "time": " 18.1",
            "now drop rate": " 2.2%"
        },
        {
            "time": " 19.1",
            "now drop rate": " 2.2%"
        },
        {
            "time": " 20.1",
            "now drop rate": " 2.1%"
        },
        {
            "time": " 21.1",
            "now drop rate": " 2.1%"
        },
        {
            "time": " 22.1",
            "now drop rate": " 2.1%"
        },
        {
            "time": " 27.8",
            "now drop rate": " 19.7%"
        },
        {
            "time": " 28.8",
            "now drop rate": " 20.8%"
        },
        {
            "time": " 29.8",
            "now drop rate": " 20.2%"
        },
        {
            "time": " 30.8",
            "now drop rate": " 19.6%"
        },
        {
            "time": " 31.8",
            "now drop rate": " 19.0%"
        },
        {
            "time": " 32.8",
            "now drop rate": " 18.4%"
        },
        {
            "time": " 33.8",
            "now drop rate": " 18.1%"
        },
        {
            "time": " 39.5",
            "now drop rate": " 28.2%"
        },
        {
            "time": " 40.5",
            "now drop rate": " 26.0%"
        },
        {
            "time": " 41.5",
            "now drop rate": " 25.4%"
        },
        {
            "time": " 42.5",
            "now drop rate": " 24.8%"
        },
        {
            "time": " 43.5",
            "now drop rate": " 24.3%"
        },
        {
            "time": " 44.5",
            "now drop rate": " 23.7%"
        },
        {
            "time": " 45.6",
            "now drop rate": " 23.2%"
        },
        {
            "time": " 46.6",
            "now drop rate": " 22.8%"
        },
        {
            "time": " 47.6",
            "now drop rate": " 22.3%"
        },
        {
            "time": " 48.6",
            "now drop rate": " 21.9%"
        },
        {
            "time": " 49.6",
            "now drop rate": " 21.5%"
        },
        {
            "time": " 50.6",
            "now drop rate": " 21.1%"
        },
        {
            "time": " 51.6",
            "now drop rate": " 20.7%"
        },
        {
            "time": " 52.6",
            "now drop rate": " 20.3%"
        },
        {
            "time": " 53.6",
            "now drop rate": " 20.0%"
        },
        {
            "time": " 54.6",
            "now drop rate": " 19.6%"
        },
        {
            "time": " 55.6",
            "now drop rate": " 19.3%"
        },
        {
            "time": " 56.6",
            "now drop rate": " 19.0%"
        },
        {
            "time": " 57.6",
            "now drop rate": " 18.7%"
        },
        {
            "time": " 58.6",
            "now drop rate": " 18.4%"
        },
        {
            "time": " 59.6",
            "now drop rate": " 18.1%"
        },
        {
            "time": " 60.6",
            "now drop rate": " 17.8%"
        },
        {
            "time": " 61.6",
            "now drop rate": " 17.6%"
        },
        {
            "time": " 62.6",
            "now drop rate": " 17.3%"
        },
        {
            "time": " 63.6",
            "now drop rate": " 17.1%"
        },
        {
            "time": " 64.6",
            "now drop rate": " 16.8%"
        },
        {
            "time": " 65.6",
            "now drop rate": " 16.6%"
        },
        {
            "time": " 66.6",
            "now drop rate": " 16.4%"
        },
        {
            "time": " 67.6",
            "now drop rate": " 16.1%"
        },
        {
            "time": " 68.6",
            "now drop rate": " 15.9%"
        },
        {
            "time": " 69.6",
            "now drop rate": " 15.7%"
        },
        {
            "time": " 70.7",
            "now drop rate": " 15.6%"
        },
        {
            "time": " 71.7",
            "now drop rate": " 15.4%"
        },
        {
            "time": " 72.7",
            "now drop rate": " 15.2%"
        },
        {
            "time": " 73.7",
            "now drop rate": " 15.0%"
        },
        {
            "time": " 74.7",
            "now drop rate": " 14.8%"
        },
        {
            "time": " 75.7",
            "now drop rate": " 14.6%"
        },
        {
            "time": " 76.7",
            "now drop rate": " 14.4%"
        },
        {
            "time": " 77.7",
            "now drop rate": " 14.3%"
        },
        {
            "time": " 78.7",
            "now drop rate": " 14.1%"
        },
        {
            "time": " 79.7",
            "now drop rate": " 14.0%"
        },
        {
            "time": " 80.7",
            "now drop rate": " 13.8%"
        },
        {
            "time": " 81.7",
            "now drop rate": " 13.7%"
        },
        {
            "time": " 82.7",
            "now drop rate": " 13.5%"
        },
        {
            "time": " 83.7",
            "now drop rate": " 13.4%"
        },
        {
            "time": " 84.7",
            "now drop rate": " 13.2%"
        },
        {
            "time": " 85.7",
            "now drop rate": " 13.1%"
        },
        {
            "time": " 86.7",
            "now drop rate": " 12.9%"
        },
        {
            "time": " 87.7",
            "now drop rate": " 12.8%"
        },
        {
            "time": " 88.7",
            "now drop rate": " 12.7%"
        },
        {
            "time": " 89.7",
            "now drop rate": " 12.6%"
        },
        {
            "time": " 90.8",
            "now drop rate": " 12.4%"
        },
        {
            "time": " 91.8",
            "now drop rate": " 12.3%"
        },
        {
            "time": " 92.8",
            "now drop rate": " 12.2%"
        },
        {
            "time": " 93.8",
            "now drop rate": " 12.1%"
        },
        {
            "time": " 94.8",
            "now drop rate": " 12.0%"
        },
        {
            "time": " 95.8",
            "now drop rate": " 11.9%"
        },
        {
            "time": " 96.8",
            "now drop rate": " 11.7%"
        },
        {
            "time": " 97.8",
            "now drop rate": " 11.6%"
        },
        {
            "time": " 98.8",
            "now drop rate": " 11.5%"
        },
        {
            "time": " 99.8",
            "now drop rate": " 11.5%"
        },
        {
            "drop rate": " 11.3%",
            "delay": " 106.8"
        }
        ],
        [
        {
            "time": " 1.0",
            "now drop rate": " 7.2%"
        },
        {
            "time": " 2.0",
            "now drop rate": " 4.3%"
        },
        {
            "time": " 3.0",
            "now drop rate": " 3.3%"
        },
        {
            "time": " 4.0",
            "now drop rate": " 2.8%"
        },
        {
            "time": " 5.0",
            "now drop rate": " 2.5%"
        },
        {
            "time": " 6.0",
            "now drop rate": " 2.4%"
        },
        {
            "time": " 7.0",
            "now drop rate": " 2.2%"
        },
        {
            "time": " 8.0",
            "now drop rate": " 2.1%"
        },
        {
            "time": " 9.0",
            "now drop rate": " 2.0%"
        },
        {
            "time": " 10.0",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 11.0",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 12.0",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 13.0",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 14.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 15.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 16.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 17.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 18.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 19.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 20.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 21.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 22.1",
            "now drop rate": " 1.7%"
        },
        {
            "time": " 23.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 24.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 25.1",
            "now drop rate": " 1.8%"
        },
        {
            "time": " 26.1",
            "now drop rate": " 1.9%"
        },
        {
            "time": " 28.3",
            "now drop rate": " 8.8%"
        },
        {
            "time": " 29.3",
            "now drop rate": " 8.7%"
        },
        {
            "time": " 30.3",
            "now drop rate": " 8.5%"
        },
        {
            "time": " 31.3",
            "now drop rate": " 8.2%"
        },
        {
            "time": " 32.3",
            "now drop rate": " 8.0%"
        },
        {
            "time": " 33.3",
            "now drop rate": " 7.8%"
        },
        {
            "time": " 39.6",
            "now drop rate": " 21.8%"
        },
        {
            "time": " 40.6",
            "now drop rate": " 19.6%"
        },
        {
            "time": " 41.6",
            "now drop rate": " 19.2%"
        },
        {
            "time": " 42.6",
            "now drop rate": " 18.8%"
        },
        {
            "time": " 43.6",
            "now drop rate": " 18.4%"
        },
        {
            "time": " 44.6",
            "now drop rate": " 18.0%"
        },
        {
            "time": " 45.6",
            "now drop rate": " 17.6%"
        },
        {
            "time": " 46.6",
            "now drop rate": " 17.3%"
        },
        {
            "time": " 47.6",
            "now drop rate": " 17.0%"
        },
        {
            "time": " 48.6",
            "now drop rate": " 16.6%"
        },
        {
            "time": " 49.6",
            "now drop rate": " 16.3%"
        },
        {
            "time": " 50.6",
            "now drop rate": " 16.0%"
        },
        {
            "time": " 51.6",
            "now drop rate": " 15.8%"
        },
        {
            "time": " 52.6",
            "now drop rate": " 15.5%"
        },
        {
            "time": " 53.6",
            "now drop rate": " 15.2%"
        },
        {
            "time": " 54.6",
            "now drop rate": " 15.0%"
        },
        {
            "time": " 55.6",
            "now drop rate": " 14.7%"
        },
        {
            "time": " 56.6",
            "now drop rate": " 14.5%"
        },
        {
            "time": " 57.6",
            "now drop rate": " 14.3%"
        },
        {
            "time": " 58.6",
            "now drop rate": " 14.0%"
        },
        {
            "time": " 59.6",
            "now drop rate": " 13.8%"
        },
        {
            "time": " 60.7",
            "now drop rate": " 13.6%"
        },
        {
            "time": " 61.7",
            "now drop rate": " 13.4%"
        },
        {
            "time": " 62.7",
            "now drop rate": " 13.2%"
        },
        {
            "time": " 63.7",
            "now drop rate": " 13.1%"
        },
        {
            "time": " 64.7",
            "now drop rate": " 12.9%"
        },
        {
            "time": " 65.7",
            "now drop rate": " 12.7%"
        },
        {
            "time": " 66.7",
            "now drop rate": " 12.5%"
        },
        {
            "time": " 67.7",
            "now drop rate": " 12.4%"
        },
        {
            "time": " 68.7",
            "now drop rate": " 12.2%"
        },
        {
            "time": " 69.7",
            "now drop rate": " 12.1%"
        },
        {
            "time": " 70.7",
            "now drop rate": " 12.0%"
        },
        {
            "time": " 71.7",
            "now drop rate": " 11.8%"
        },
        {
            "time": " 72.7",
            "now drop rate": " 11.7%"
        },
        {
            "time": " 73.7",
            "now drop rate": " 11.5%"
        },
        {
            "time": " 74.7",
            "now drop rate": " 11.4%"
        },
        {
            "time": " 75.7",
            "now drop rate": " 11.3%"
        },
        {
            "time": " 76.7",
            "now drop rate": " 11.1%"
        },
        {
            "time": " 77.7",
            "now drop rate": " 11.0%"
        },
        {
            "time": " 78.7",
            "now drop rate": " 10.9%"
        },
        {
            "time": " 79.7",
            "now drop rate": " 10.8%"
        },
        {
            "time": " 80.7",
            "now drop rate": " 10.7%"
        },
        {
            "time": " 81.8",
            "now drop rate": " 10.6%"
        },
        {
            "time": " 82.8",
            "now drop rate": " 10.5%"
        },
        {
            "time": " 83.8",
            "now drop rate": " 10.4%"
        },
        {
            "time": " 84.8",
            "now drop rate": " 10.3%"
        },
        {
            "time": " 85.8",
            "now drop rate": " 10.1%"
        },
        {
            "time": " 86.8",
            "now drop rate": " 10.0%"
        },
        {
            "time": " 87.8",
            "now drop rate": " 9.9%"
        },
        {
            "time": " 88.8",
            "now drop rate": " 9.8%"
        },
        {
            "time": " 89.8",
            "now drop rate": " 9.7%"
        },
        {
            "time": " 90.8",
            "now drop rate": " 9.6%"
        },
        {
            "time": " 91.8",
            "now drop rate": " 9.6%"
        },
        {
            "time": " 92.8",
            "now drop rate": " 9.5%"
        },
        {
            "time": " 93.8",
            "now drop rate": " 9.4%"
        },
        {
            "time": " 94.8",
            "now drop rate": " 9.3%"
        },
        {
            "time": " 95.8",
            "now drop rate": " 9.2%"
        },
        {
            "time": " 96.8",
            "now drop rate": " 9.1%"
        },
        {
            "time": " 97.8",
            "now drop rate": " 9.1%"
        },
        {
            "time": " 98.8",
            "now drop rate": " 9.0%"
        },
        {
            "time": " 99.8",
            "now drop rate": " 8.9%"
        },
        {
            "drop rate": " 8.8%",
            "delay": " 107.1"
        }
        ]
    ],
    "n=1": [
[
  {
    "time": " 1.0",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 28.2",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 29.2",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 30.2",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 31.3",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 32.3",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 33.3",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 34.3",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 35.3",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 36.3",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 37.3",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 38.3",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 39.3",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 40.3",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 41.3",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 42.3",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 43.3",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 44.3",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 45.3",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 46.3",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 47.3",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 48.3",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 49.3",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 50.3",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 51.3",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 52.3",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 53.4",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 54.4",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 55.4",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 56.4",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 57.4",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 58.4",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 59.4",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 60.4",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 61.4",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 62.4",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 63.4",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 64.4",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 65.4",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 66.4",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 67.4",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 68.4",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 69.4",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 70.4",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 71.4",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 72.4",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 73.4",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 74.5",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 75.5",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 76.5",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 77.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 78.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 79.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 80.5",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 81.5",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 82.5",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 83.5",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 84.5",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 85.5",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 86.5",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 87.5",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 88.5",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 89.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 90.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 91.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 92.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 93.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 94.6",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 95.6",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 96.6",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 97.6",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 98.6",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 99.6",
    "now drop rate": " 3.7%"
  },
  {
    "drop rate": " 3.6%",
    "delay": " 105.8"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 27.2",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 28.2",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 29.2",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 30.2",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 31.2",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 32.2",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 33.2",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 34.2",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 35.2",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 36.2",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 37.2",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 38.2",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 39.2",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 40.2",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 41.2",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 42.2",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 43.2",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 44.2",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 45.3",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 46.3",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 47.3",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 48.3",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 49.3",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 50.3",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 51.3",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 52.3",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 53.3",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 54.3",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 55.3",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 56.3",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 57.3",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 58.3",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 59.3",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 60.3",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 61.3",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 62.3",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 63.3",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 64.3",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 65.3",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 66.3",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 67.4",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 68.4",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 69.4",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 70.4",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 71.4",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 72.4",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 73.4",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 74.4",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 75.4",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 76.4",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 77.4",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 78.4",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 79.4",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 80.4",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 81.4",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 82.4",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 83.4",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 84.4",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 85.4",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 86.4",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 87.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 88.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 89.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 90.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 91.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 92.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 93.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 94.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 95.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 96.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 97.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 98.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 99.5",
    "now drop rate": " 3.7%"
  },
  {
    "drop rate": " 3.6%",
    "delay": " 107.4"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 25.7",
    "now drop rate": " 13.3%"
  },
  {
    "time": " 27.2",
    "now drop rate": " 14.0%"
  },
  {
    "time": " 28.2",
    "now drop rate": " 16.9%"
  },
  {
    "time": " 29.2",
    "now drop rate": " 16.5%"
  },
  {
    "time": " 30.2",
    "now drop rate": " 16.0%"
  },
  {
    "time": " 31.3",
    "now drop rate": " 15.5%"
  },
  {
    "time": " 32.3",
    "now drop rate": " 15.1%"
  },
  {
    "time": " 33.3",
    "now drop rate": " 14.7%"
  },
  {
    "time": " 37.5",
    "now drop rate": " 23.7%"
  },
  {
    "time": " 38.5",
    "now drop rate": " 22.2%"
  },
  {
    "time": " 39.5",
    "now drop rate": " 21.7%"
  },
  {
    "time": " 40.5",
    "now drop rate": " 21.1%"
  },
  {
    "time": " 41.5",
    "now drop rate": " 20.6%"
  },
  {
    "time": " 42.5",
    "now drop rate": " 20.2%"
  },
  {
    "time": " 43.5",
    "now drop rate": " 19.8%"
  },
  {
    "time": " 44.5",
    "now drop rate": " 19.3%"
  },
  {
    "time": " 45.5",
    "now drop rate": " 18.9%"
  },
  {
    "time": " 46.5",
    "now drop rate": " 18.6%"
  },
  {
    "time": " 47.5",
    "now drop rate": " 18.2%"
  },
  {
    "time": " 48.5",
    "now drop rate": " 17.9%"
  },
  {
    "time": " 49.5",
    "now drop rate": " 17.5%"
  },
  {
    "time": " 50.5",
    "now drop rate": " 17.2%"
  },
  {
    "time": " 51.5",
    "now drop rate": " 16.9%"
  },
  {
    "time": " 52.5",
    "now drop rate": " 16.6%"
  },
  {
    "time": " 53.5",
    "now drop rate": " 16.3%"
  },
  {
    "time": " 54.5",
    "now drop rate": " 16.0%"
  },
  {
    "time": " 55.6",
    "now drop rate": " 15.8%"
  },
  {
    "time": " 56.6",
    "now drop rate": " 15.5%"
  },
  {
    "time": " 57.6",
    "now drop rate": " 15.3%"
  },
  {
    "time": " 58.6",
    "now drop rate": " 15.0%"
  },
  {
    "time": " 59.6",
    "now drop rate": " 14.8%"
  },
  {
    "time": " 60.6",
    "now drop rate": " 14.6%"
  },
  {
    "time": " 61.6",
    "now drop rate": " 14.4%"
  },
  {
    "time": " 62.6",
    "now drop rate": " 14.2%"
  },
  {
    "time": " 63.6",
    "now drop rate": " 14.0%"
  },
  {
    "time": " 64.6",
    "now drop rate": " 13.8%"
  },
  {
    "time": " 65.6",
    "now drop rate": " 13.6%"
  },
  {
    "time": " 66.6",
    "now drop rate": " 13.4%"
  },
  {
    "time": " 67.6",
    "now drop rate": " 13.2%"
  },
  {
    "time": " 68.6",
    "now drop rate": " 13.0%"
  },
  {
    "time": " 69.6",
    "now drop rate": " 12.9%"
  },
  {
    "time": " 76.5",
    "now drop rate": " 19.6%"
  },
  {
    "time": " 77.5",
    "now drop rate": " 18.5%"
  },
  {
    "time": " 78.5",
    "now drop rate": " 18.3%"
  },
  {
    "time": " 79.5",
    "now drop rate": " 18.1%"
  },
  {
    "time": " 80.5",
    "now drop rate": " 17.9%"
  },
  {
    "time": " 81.5",
    "now drop rate": " 17.7%"
  },
  {
    "time": " 82.5",
    "now drop rate": " 17.5%"
  },
  {
    "time": " 83.5",
    "now drop rate": " 17.3%"
  },
  {
    "time": " 84.5",
    "now drop rate": " 17.1%"
  },
  {
    "time": " 85.5",
    "now drop rate": " 16.9%"
  },
  {
    "time": " 86.5",
    "now drop rate": " 16.7%"
  },
  {
    "time": " 87.5",
    "now drop rate": " 16.6%"
  },
  {
    "time": " 88.6",
    "now drop rate": " 16.4%"
  },
  {
    "time": " 89.6",
    "now drop rate": " 16.2%"
  },
  {
    "time": " 90.6",
    "now drop rate": " 16.1%"
  },
  {
    "time": " 91.6",
    "now drop rate": " 15.9%"
  },
  {
    "time": " 92.6",
    "now drop rate": " 15.8%"
  },
  {
    "time": " 93.6",
    "now drop rate": " 15.6%"
  },
  {
    "time": " 94.6",
    "now drop rate": " 15.4%"
  },
  {
    "time": " 95.6",
    "now drop rate": " 15.3%"
  },
  {
    "time": " 96.6",
    "now drop rate": " 15.1%"
  },
  {
    "time": " 97.6",
    "now drop rate": " 15.0%"
  },
  {
    "time": " 98.6",
    "now drop rate": " 14.9%"
  },
  {
    "time": " 99.6",
    "now drop rate": " 14.7%"
  },
  {
    "drop rate": " 14.6%",
    "delay": " 114.0"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 27.3",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 28.3",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 29.3",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 30.3",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 31.3",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 32.3",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 33.3",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 36.5",
    "now drop rate": " 15.2%"
  },
  {
    "time": " 37.5",
    "now drop rate": " 13.9%"
  },
  {
    "time": " 38.5",
    "now drop rate": " 13.5%"
  },
  {
    "time": " 39.5",
    "now drop rate": " 13.2%"
  },
  {
    "time": " 40.5",
    "now drop rate": " 12.9%"
  },
  {
    "time": " 41.5",
    "now drop rate": " 12.6%"
  },
  {
    "time": " 42.5",
    "now drop rate": " 12.4%"
  },
  {
    "time": " 43.6",
    "now drop rate": " 12.1%"
  },
  {
    "time": " 44.6",
    "now drop rate": " 11.9%"
  },
  {
    "time": " 45.6",
    "now drop rate": " 11.6%"
  },
  {
    "time": " 46.6",
    "now drop rate": " 11.4%"
  },
  {
    "time": " 47.6",
    "now drop rate": " 11.2%"
  },
  {
    "time": " 48.6",
    "now drop rate": " 11.0%"
  },
  {
    "time": " 49.6",
    "now drop rate": " 10.8%"
  },
  {
    "time": " 50.6",
    "now drop rate": " 10.6%"
  },
  {
    "time": " 51.6",
    "now drop rate": " 10.5%"
  },
  {
    "time": " 52.6",
    "now drop rate": " 10.3%"
  },
  {
    "time": " 53.6",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 54.6",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 55.6",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 56.6",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 57.6",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 58.6",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 59.6",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 60.6",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 61.6",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 62.6",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 63.6",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 64.6",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 65.6",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 66.7",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 67.7",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 68.7",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 69.7",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 76.5",
    "now drop rate": " 15.3%"
  },
  {
    "time": " 77.5",
    "now drop rate": " 14.2%"
  },
  {
    "time": " 78.5",
    "now drop rate": " 14.1%"
  },
  {
    "time": " 79.5",
    "now drop rate": " 14.0%"
  },
  {
    "time": " 80.5",
    "now drop rate": " 13.8%"
  },
  {
    "time": " 81.5",
    "now drop rate": " 13.7%"
  },
  {
    "time": " 82.6",
    "now drop rate": " 13.5%"
  },
  {
    "time": " 83.6",
    "now drop rate": " 13.4%"
  },
  {
    "time": " 84.6",
    "now drop rate": " 13.2%"
  },
  {
    "time": " 85.6",
    "now drop rate": " 13.1%"
  },
  {
    "time": " 86.6",
    "now drop rate": " 12.9%"
  },
  {
    "time": " 87.6",
    "now drop rate": " 12.8%"
  },
  {
    "time": " 88.6",
    "now drop rate": " 12.7%"
  },
  {
    "time": " 89.6",
    "now drop rate": " 12.6%"
  },
  {
    "time": " 90.6",
    "now drop rate": " 12.4%"
  },
  {
    "time": " 91.6",
    "now drop rate": " 12.3%"
  },
  {
    "time": " 92.6",
    "now drop rate": " 12.2%"
  },
  {
    "time": " 93.6",
    "now drop rate": " 12.1%"
  },
  {
    "time": " 94.6",
    "now drop rate": " 12.0%"
  },
  {
    "time": " 95.6",
    "now drop rate": " 11.9%"
  },
  {
    "time": " 96.6",
    "now drop rate": " 11.7%"
  },
  {
    "time": " 97.6",
    "now drop rate": " 11.6%"
  },
  {
    "time": " 98.6",
    "now drop rate": " 11.5%"
  },
  {
    "time": " 99.6",
    "now drop rate": " 11.4%"
  },
  {
    "drop rate": " 11.3%",
    "delay": " 110.7"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 10.5%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 31.2",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 32.2",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 33.2",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 37.4",
    "now drop rate": " 17.6%"
  },
  {
    "time": " 38.4",
    "now drop rate": " 16.2%"
  },
  {
    "time": " 39.4",
    "now drop rate": " 15.8%"
  },
  {
    "time": " 40.4",
    "now drop rate": " 15.4%"
  },
  {
    "time": " 41.4",
    "now drop rate": " 15.1%"
  },
  {
    "time": " 42.4",
    "now drop rate": " 14.8%"
  },
  {
    "time": " 43.4",
    "now drop rate": " 14.5%"
  },
  {
    "time": " 44.4",
    "now drop rate": " 14.2%"
  },
  {
    "time": " 45.4",
    "now drop rate": " 13.9%"
  },
  {
    "time": " 46.4",
    "now drop rate": " 13.6%"
  },
  {
    "time": " 47.4",
    "now drop rate": " 13.4%"
  },
  {
    "time": " 48.4",
    "now drop rate": " 13.1%"
  },
  {
    "time": " 49.4",
    "now drop rate": " 12.9%"
  },
  {
    "time": " 50.4",
    "now drop rate": " 12.7%"
  },
  {
    "time": " 51.4",
    "now drop rate": " 12.5%"
  },
  {
    "time": " 52.4",
    "now drop rate": " 12.3%"
  },
  {
    "time": " 53.5",
    "now drop rate": " 12.1%"
  },
  {
    "time": " 54.5",
    "now drop rate": " 11.9%"
  },
  {
    "time": " 55.5",
    "now drop rate": " 11.7%"
  },
  {
    "time": " 56.5",
    "now drop rate": " 11.5%"
  },
  {
    "time": " 57.5",
    "now drop rate": " 11.4%"
  },
  {
    "time": " 58.5",
    "now drop rate": " 11.2%"
  },
  {
    "time": " 59.5",
    "now drop rate": " 11.0%"
  },
  {
    "time": " 60.5",
    "now drop rate": " 10.9%"
  },
  {
    "time": " 61.5",
    "now drop rate": " 10.7%"
  },
  {
    "time": " 62.5",
    "now drop rate": " 10.6%"
  },
  {
    "time": " 63.5",
    "now drop rate": " 10.4%"
  },
  {
    "time": " 64.5",
    "now drop rate": " 10.3%"
  },
  {
    "time": " 65.5",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 66.5",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 67.5",
    "now drop rate": " 9.9%"
  },
  {
    "time": " 68.5",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 69.5",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 70.5",
    "now drop rate": " 9.6%"
  },
  {
    "time": " 71.5",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 72.5",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 73.5",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 74.5",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 75.6",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 76.6",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 77.6",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 78.6",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 79.6",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 80.6",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 81.6",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 82.6",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 83.6",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 84.6",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 85.6",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 86.6",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 87.6",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 88.6",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 89.6",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 90.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 91.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 92.6",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 93.7",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 94.7",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 95.7",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 96.7",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 97.7",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 98.7",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 99.7",
    "now drop rate": " 7.3%"
  },
  {
    "drop rate": " 7.2%",
    "delay": " 108.4"
  }
]
    ],
    "n=2": [
[
  {
    "time": " 1.0",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 33.1",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 34.4",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 35.4",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 36.4",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 37.4",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 38.4",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 39.4",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 40.4",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 41.4",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 42.4",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 43.4",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 44.4",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 45.4",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 46.4",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 47.4",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 48.4",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 49.4",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 50.5",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 51.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 52.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 53.5",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 54.5",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 55.5",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 56.5",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 57.5",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 58.5",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 59.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 60.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 61.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 62.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 63.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 64.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 65.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 66.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 67.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 68.5",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 69.5",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 70.5",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 71.5",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 72.5",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 73.6",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 74.6",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 75.6",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 76.6",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 77.6",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 78.6",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 79.6",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 80.6",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 81.6",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 82.6",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 83.6",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 84.6",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 85.6",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 86.6",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 87.6",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 88.7",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 89.7",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 90.7",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 91.7",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 92.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 93.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 94.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 95.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 96.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 97.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 98.7",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 99.7",
    "now drop rate": " 3.0%"
  },
  {
    "drop rate": " 2.9%",
    "delay": " 107.0"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 13.0",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 14.0",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 25.6",
    "now drop rate": " 13.2%"
  },
  {
    "time": " 26.6",
    "now drop rate": " 10.8%"
  },
  {
    "time": " 27.6",
    "now drop rate": " 10.4%"
  },
  {
    "time": " 28.6",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 29.7",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 30.7",
    "now drop rate": " 9.6%"
  },
  {
    "time": " 31.7",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 32.7",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 33.7",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 36.5",
    "now drop rate": " 14.2%"
  },
  {
    "time": " 37.5",
    "now drop rate": " 13.9%"
  },
  {
    "time": " 38.5",
    "now drop rate": " 13.6%"
  },
  {
    "time": " 39.5",
    "now drop rate": " 13.3%"
  },
  {
    "time": " 40.5",
    "now drop rate": " 13.0%"
  },
  {
    "time": " 41.5",
    "now drop rate": " 12.7%"
  },
  {
    "time": " 42.5",
    "now drop rate": " 12.4%"
  },
  {
    "time": " 43.5",
    "now drop rate": " 12.2%"
  },
  {
    "time": " 44.5",
    "now drop rate": " 11.9%"
  },
  {
    "time": " 45.5",
    "now drop rate": " 11.7%"
  },
  {
    "time": " 46.5",
    "now drop rate": " 11.5%"
  },
  {
    "time": " 47.5",
    "now drop rate": " 11.3%"
  },
  {
    "time": " 48.5",
    "now drop rate": " 11.1%"
  },
  {
    "time": " 49.5",
    "now drop rate": " 10.9%"
  },
  {
    "time": " 50.5",
    "now drop rate": " 10.7%"
  },
  {
    "time": " 51.6",
    "now drop rate": " 10.5%"
  },
  {
    "time": " 52.6",
    "now drop rate": " 10.3%"
  },
  {
    "time": " 53.6",
    "now drop rate": " 10.2%"
  },
  {
    "time": " 54.6",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 55.6",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 56.6",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 57.6",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 58.6",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 59.6",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 60.6",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 61.6",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 62.6",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 63.6",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 64.6",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 65.6",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 66.6",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 67.6",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 68.6",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 69.6",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 70.6",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 71.6",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 72.6",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 73.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 74.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 75.7",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 76.7",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 77.7",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 78.7",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 79.7",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 80.7",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 81.7",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 82.7",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 83.7",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 84.7",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 85.7",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 86.7",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 87.7",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 88.7",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 89.7",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 90.7",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 91.7",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 92.7",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 93.7",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 94.7",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 95.8",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 96.8",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 97.8",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 98.8",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 99.8",
    "now drop rate": " 6.2%"
  },
  {
    "drop rate": " 6.1%",
    "delay": " 112.3"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 8.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 9.1",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 10.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 30.2",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 31.2",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 32.2",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 33.2",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 34.2",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 36.5",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 37.5",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 38.5",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 39.5",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 40.5",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 41.5",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 42.6",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 43.6",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 44.6",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 45.6",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 46.6",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 47.6",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 48.6",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 49.6",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 50.6",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 51.6",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 52.6",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 53.6",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 54.6",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 55.6",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 56.6",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 57.6",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 58.6",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 59.6",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 60.6",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 61.6",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 62.6",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 63.6",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 64.6",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 65.6",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 66.6",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 67.6",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 68.6",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 69.7",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 70.7",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 71.7",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 72.7",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 73.7",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 74.7",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 75.7",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 76.7",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 77.7",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 78.7",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 79.7",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 80.7",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 81.7",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 82.7",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 83.7",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 84.7",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 85.7",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 86.7",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 87.7",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 88.7",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 89.8",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 90.8",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 91.8",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 92.8",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 93.8",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 94.8",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 95.8",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 96.8",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 97.8",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 98.8",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 99.8",
    "now drop rate": " 4.1%"
  },
  {
    "drop rate": " 4.0%",
    "delay": " 109.1"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 33.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 34.5",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 36.6",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 37.6",
    "now drop rate": " 9.9%"
  },
  {
    "time": " 38.6",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 39.6",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 40.6",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 41.6",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 42.6",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 43.6",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 44.6",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 45.6",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 46.6",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 47.6",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 48.6",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 49.6",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 50.6",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 51.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 52.7",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 53.7",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 54.7",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 55.7",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 56.7",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 57.7",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 58.7",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 59.7",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 60.7",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 61.7",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 62.7",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 63.7",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 64.7",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 65.7",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 66.7",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 67.7",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 68.7",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 69.7",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 70.7",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 71.7",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 72.7",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 73.7",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 74.7",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 75.7",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 76.7",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 77.8",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 78.8",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 79.8",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 80.8",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 81.8",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 82.8",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 83.8",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 84.8",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 85.8",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 86.8",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 87.8",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 88.8",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 89.8",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 90.8",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 91.8",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 92.8",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 93.8",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 94.8",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 95.8",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 96.8",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 97.8",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 98.8",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 99.8",
    "now drop rate": " 4.8%"
  },
  {
    "drop rate": " 4.7%",
    "delay": " 109.2"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.6%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 25.8",
    "now drop rate": " 13.4%"
  },
  {
    "time": " 26.8",
    "now drop rate": " 11.0%"
  },
  {
    "time": " 27.8",
    "now drop rate": " 10.7%"
  },
  {
    "time": " 28.8",
    "now drop rate": " 10.3%"
  },
  {
    "time": " 29.8",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 30.8",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 31.8",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 32.8",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 36.5",
    "now drop rate": " 16.6%"
  },
  {
    "time": " 37.5",
    "now drop rate": " 16.4%"
  },
  {
    "time": " 38.5",
    "now drop rate": " 16.0%"
  },
  {
    "time": " 39.5",
    "now drop rate": " 15.7%"
  },
  {
    "time": " 40.5",
    "now drop rate": " 15.3%"
  },
  {
    "time": " 41.5",
    "now drop rate": " 14.9%"
  },
  {
    "time": " 42.6",
    "now drop rate": " 14.6%"
  },
  {
    "time": " 43.6",
    "now drop rate": " 14.3%"
  },
  {
    "time": " 44.6",
    "now drop rate": " 14.0%"
  },
  {
    "time": " 45.6",
    "now drop rate": " 13.8%"
  },
  {
    "time": " 46.6",
    "now drop rate": " 13.5%"
  },
  {
    "time": " 47.6",
    "now drop rate": " 13.2%"
  },
  {
    "time": " 48.6",
    "now drop rate": " 13.0%"
  },
  {
    "time": " 49.6",
    "now drop rate": " 12.8%"
  },
  {
    "time": " 50.6",
    "now drop rate": " 12.5%"
  },
  {
    "time": " 51.6",
    "now drop rate": " 12.3%"
  },
  {
    "time": " 52.6",
    "now drop rate": " 12.1%"
  },
  {
    "time": " 53.6",
    "now drop rate": " 11.9%"
  },
  {
    "time": " 54.6",
    "now drop rate": " 11.7%"
  },
  {
    "time": " 55.6",
    "now drop rate": " 11.6%"
  },
  {
    "time": " 56.6",
    "now drop rate": " 11.4%"
  },
  {
    "time": " 57.6",
    "now drop rate": " 11.2%"
  },
  {
    "time": " 58.6",
    "now drop rate": " 11.1%"
  },
  {
    "time": " 59.6",
    "now drop rate": " 10.9%"
  },
  {
    "time": " 60.6",
    "now drop rate": " 10.7%"
  },
  {
    "time": " 61.6",
    "now drop rate": " 10.6%"
  },
  {
    "time": " 62.7",
    "now drop rate": " 10.5%"
  },
  {
    "time": " 63.7",
    "now drop rate": " 10.4%"
  },
  {
    "time": " 64.7",
    "now drop rate": " 10.2%"
  },
  {
    "time": " 65.7",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 66.7",
    "now drop rate": " 9.9%"
  },
  {
    "time": " 67.7",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 68.7",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 69.7",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 70.7",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 71.7",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 72.7",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 73.7",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 74.7",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 75.7",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 76.7",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 77.7",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 78.7",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 79.7",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 80.7",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 81.7",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 82.7",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 83.7",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 84.7",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 85.7",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 86.7",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 87.7",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 88.7",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 89.8",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 90.8",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 91.8",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 92.8",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 93.8",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 94.8",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 95.8",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 96.8",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 97.8",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 98.8",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 99.8",
    "now drop rate": " 7.1%"
  },
  {
    "drop rate": " 7.0%",
    "delay": " 111.7"
  }
]
    ],
    "n=3": [
[
  {
    "time": " 1.0",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.2",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 22.2",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 26.8",
    "now drop rate": " 16.7%"
  },
  {
    "time": " 27.8",
    "now drop rate": " 16.3%"
  },
  {
    "time": " 28.8",
    "now drop rate": " 15.8%"
  },
  {
    "time": " 29.8",
    "now drop rate": " 15.3%"
  },
  {
    "time": " 30.8",
    "now drop rate": " 14.9%"
  },
  {
    "time": " 31.8",
    "now drop rate": " 14.4%"
  },
  {
    "time": " 32.8",
    "now drop rate": " 14.1%"
  },
  {
    "time": " 34.5",
    "now drop rate": " 16.3%"
  },
  {
    "time": " 35.5",
    "now drop rate": " 15.5%"
  },
  {
    "time": " 36.5",
    "now drop rate": " 15.1%"
  },
  {
    "time": " 37.6",
    "now drop rate": " 14.8%"
  },
  {
    "time": " 38.6",
    "now drop rate": " 14.5%"
  },
  {
    "time": " 39.6",
    "now drop rate": " 14.2%"
  },
  {
    "time": " 40.6",
    "now drop rate": " 13.8%"
  },
  {
    "time": " 41.6",
    "now drop rate": " 13.5%"
  },
  {
    "time": " 42.6",
    "now drop rate": " 13.2%"
  },
  {
    "time": " 43.6",
    "now drop rate": " 12.9%"
  },
  {
    "time": " 44.6",
    "now drop rate": " 12.7%"
  },
  {
    "time": " 45.6",
    "now drop rate": " 12.4%"
  },
  {
    "time": " 46.6",
    "now drop rate": " 12.2%"
  },
  {
    "time": " 47.6",
    "now drop rate": " 12.0%"
  },
  {
    "time": " 48.6",
    "now drop rate": " 11.7%"
  },
  {
    "time": " 49.6",
    "now drop rate": " 11.5%"
  },
  {
    "time": " 50.6",
    "now drop rate": " 11.3%"
  },
  {
    "time": " 51.6",
    "now drop rate": " 11.1%"
  },
  {
    "time": " 52.6",
    "now drop rate": " 11.0%"
  },
  {
    "time": " 53.6",
    "now drop rate": " 10.8%"
  },
  {
    "time": " 54.6",
    "now drop rate": " 10.6%"
  },
  {
    "time": " 55.6",
    "now drop rate": " 10.5%"
  },
  {
    "time": " 56.6",
    "now drop rate": " 10.3%"
  },
  {
    "time": " 57.7",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 58.7",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 59.7",
    "now drop rate": " 9.9%"
  },
  {
    "time": " 60.7",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 61.7",
    "now drop rate": " 9.6%"
  },
  {
    "time": " 62.7",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 63.7",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 64.7",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 65.7",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 66.7",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 67.7",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 68.7",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 69.7",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 70.7",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 71.7",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 72.7",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 73.7",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 74.7",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 75.7",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 76.7",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 77.7",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 78.7",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 79.8",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 80.8",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 81.8",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 82.8",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 83.8",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 84.8",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 85.8",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 86.8",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 87.8",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 88.8",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 89.8",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 90.8",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 91.8",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 92.8",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 93.8",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 94.8",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 95.8",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 96.8",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 97.8",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 98.8",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 99.8",
    "now drop rate": " 6.5%"
  },
  {
    "drop rate": " 6.5%",
    "delay": " 108.8"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 24.7",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 25.7",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 26.7",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 27.7",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 28.7",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 29.7",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 30.7",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 31.7",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 32.7",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 34.5",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 35.5",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 36.5",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 37.5",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 38.6",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 39.6",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 40.6",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 41.6",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 42.6",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 43.6",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 44.6",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 45.6",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 46.6",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 47.6",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 48.6",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 49.6",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 50.6",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 51.6",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 52.6",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 53.6",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 54.6",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 55.6",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 56.6",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 57.6",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 58.6",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 59.7",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 60.7",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 61.7",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 62.7",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 63.7",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 64.7",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 65.7",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 66.7",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 67.7",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 68.7",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 69.7",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 70.7",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 71.7",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 72.7",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 73.7",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 74.7",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 75.7",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 76.7",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 77.7",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 78.7",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 79.7",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 80.7",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 81.7",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 82.7",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 83.7",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 84.7",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 85.7",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 86.7",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 87.7",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 88.8",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 89.8",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 90.8",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 91.8",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 92.8",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 93.8",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 94.8",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 95.8",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 96.8",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 97.8",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 98.8",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 99.8",
    "now drop rate": " 3.9%"
  },
  {
    "drop rate": " 3.8%",
    "delay": " 111.9"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 24.6",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 25.6",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 26.6",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 27.6",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 28.6",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 29.6",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 30.6",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 31.6",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 32.6",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 33.6",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 34.6",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 35.6",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 36.6",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 37.6",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 38.6",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 39.6",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 40.6",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 41.6",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 42.7",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 43.7",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 44.7",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 45.7",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 46.7",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 47.7",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 48.7",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 49.7",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 50.7",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 51.7",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 52.7",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 53.7",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 54.7",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 55.7",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 56.7",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 57.7",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 58.7",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 59.7",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 60.7",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 61.7",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 62.7",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 63.8",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 64.8",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 65.8",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 66.8",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 67.8",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 68.8",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 69.8",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 70.8",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 71.8",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 72.8",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 73.8",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 74.8",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 75.8",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 76.8",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 77.8",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 78.8",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 79.8",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 80.8",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 81.8",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 82.8",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 83.8",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 84.8",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 85.8",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 86.8",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 87.8",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 88.9",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 89.9",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 90.9",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 91.9",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 92.9",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 93.9",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 94.9",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 95.9",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 96.9",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 97.9",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 98.9",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 99.9",
    "now drop rate": " 3.1%"
  },
  {
    "drop rate": " 3.0%",
    "delay": " 109.0"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 9.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 10.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 25.5",
    "now drop rate": " 13.4%"
  },
  {
    "time": " 26.5",
    "now drop rate": " 15.9%"
  },
  {
    "time": " 27.5",
    "now drop rate": " 15.4%"
  },
  {
    "time": " 28.5",
    "now drop rate": " 14.9%"
  },
  {
    "time": " 29.6",
    "now drop rate": " 14.4%"
  },
  {
    "time": " 30.6",
    "now drop rate": " 14.0%"
  },
  {
    "time": " 31.6",
    "now drop rate": " 13.6%"
  },
  {
    "time": " 32.6",
    "now drop rate": " 13.3%"
  },
  {
    "time": " 34.4",
    "now drop rate": " 15.8%"
  },
  {
    "time": " 35.4",
    "now drop rate": " 14.4%"
  },
  {
    "time": " 36.4",
    "now drop rate": " 14.0%"
  },
  {
    "time": " 37.4",
    "now drop rate": " 13.7%"
  },
  {
    "time": " 38.4",
    "now drop rate": " 13.4%"
  },
  {
    "time": " 39.5",
    "now drop rate": " 13.0%"
  },
  {
    "time": " 40.5",
    "now drop rate": " 12.7%"
  },
  {
    "time": " 41.5",
    "now drop rate": " 12.5%"
  },
  {
    "time": " 42.5",
    "now drop rate": " 12.2%"
  },
  {
    "time": " 43.5",
    "now drop rate": " 12.0%"
  },
  {
    "time": " 44.5",
    "now drop rate": " 11.7%"
  },
  {
    "time": " 45.5",
    "now drop rate": " 11.6%"
  },
  {
    "time": " 46.5",
    "now drop rate": " 11.4%"
  },
  {
    "time": " 47.5",
    "now drop rate": " 11.1%"
  },
  {
    "time": " 48.5",
    "now drop rate": " 10.9%"
  },
  {
    "time": " 49.5",
    "now drop rate": " 10.7%"
  },
  {
    "time": " 50.5",
    "now drop rate": " 10.5%"
  },
  {
    "time": " 51.5",
    "now drop rate": " 10.3%"
  },
  {
    "time": " 52.5",
    "now drop rate": " 10.2%"
  },
  {
    "time": " 53.5",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 54.5",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 55.5",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 56.5",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 57.5",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 58.5",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 59.5",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 60.5",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 61.6",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 62.6",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 63.6",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 64.6",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 65.6",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 66.6",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 67.6",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 68.6",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 69.6",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 70.6",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 71.6",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 72.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 73.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 74.6",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 75.6",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 76.6",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 77.6",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 78.6",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 79.7",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 80.7",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 81.7",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 82.7",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 83.7",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 84.7",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 85.7",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 86.7",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 87.7",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 88.7",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 89.7",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 90.7",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 91.7",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 92.7",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 93.7",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 94.7",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 95.7",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 96.7",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 97.7",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 98.7",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 99.7",
    "now drop rate": " 6.1%"
  },
  {
    "drop rate": " 6.0%",
    "delay": " 108.6"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 33.1",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 34.4",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 35.4",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 36.4",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 37.5",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 38.5",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 39.5",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 40.5",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 41.5",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 42.5",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 43.5",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 44.5",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 45.5",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 46.5",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 47.5",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 48.5",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 49.5",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 50.5",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 51.5",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 52.6",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 53.6",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 54.6",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 55.6",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 56.6",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 57.6",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 58.6",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 59.6",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 60.6",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 61.6",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 62.6",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 63.6",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 64.6",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 65.6",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 66.6",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 67.6",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 68.6",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 69.6",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 70.6",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 71.6",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 72.6",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 73.6",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 74.6",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 75.6",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 76.7",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 77.7",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 78.7",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 79.7",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 80.7",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 81.7",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 82.7",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 83.7",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 84.7",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 85.7",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 86.7",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 87.7",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 88.7",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 89.7",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 90.7",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 91.7",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 92.7",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 93.7",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 94.7",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 95.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 96.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 97.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 98.7",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 99.7",
    "now drop rate": " 3.1%"
  },
  {
    "drop rate": " 3.0%",
    "delay": " 107.8"
  }
]
    ],
    "n=4": [
[
  {
    "time": " 1.0",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 26.7",
    "now drop rate": " 16.4%"
  },
  {
    "time": " 27.7",
    "now drop rate": " 16.1%"
  },
  {
    "time": " 28.7",
    "now drop rate": " 15.6%"
  },
  {
    "time": " 29.7",
    "now drop rate": " 15.1%"
  },
  {
    "time": " 30.7",
    "now drop rate": " 14.6%"
  },
  {
    "time": " 31.7",
    "now drop rate": " 14.2%"
  },
  {
    "time": " 32.7",
    "now drop rate": " 13.9%"
  },
  {
    "time": " 33.7",
    "now drop rate": " 13.7%"
  },
  {
    "time": " 34.8",
    "now drop rate": " 13.4%"
  },
  {
    "time": " 35.8",
    "now drop rate": " 13.0%"
  },
  {
    "time": " 36.8",
    "now drop rate": " 12.7%"
  },
  {
    "time": " 37.8",
    "now drop rate": " 12.4%"
  },
  {
    "time": " 38.8",
    "now drop rate": " 12.1%"
  },
  {
    "time": " 39.8",
    "now drop rate": " 11.8%"
  },
  {
    "time": " 40.8",
    "now drop rate": " 11.5%"
  },
  {
    "time": " 41.8",
    "now drop rate": " 11.3%"
  },
  {
    "time": " 42.8",
    "now drop rate": " 11.1%"
  },
  {
    "time": " 43.8",
    "now drop rate": " 10.9%"
  },
  {
    "time": " 44.8",
    "now drop rate": " 10.7%"
  },
  {
    "time": " 45.8",
    "now drop rate": " 10.4%"
  },
  {
    "time": " 46.8",
    "now drop rate": " 10.3%"
  },
  {
    "time": " 47.8",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 48.8",
    "now drop rate": " 9.9%"
  },
  {
    "time": " 49.8",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 50.8",
    "now drop rate": " 9.6%"
  },
  {
    "time": " 51.8",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 52.8",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 53.8",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 54.8",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 55.9",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 56.9",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 57.9",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 58.9",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 59.9",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 60.9",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 61.9",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 62.9",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 63.9",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 64.9",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 65.9",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 66.9",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 67.9",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 68.9",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 69.9",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 70.9",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 71.9",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 72.9",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 74.0",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 75.0",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 76.0",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 77.0",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 78.0",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 79.0",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 80.0",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 81.0",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 82.0",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 83.0",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 84.0",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 85.0",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 86.0",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 87.0",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 88.0",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 89.0",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 90.0",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 91.0",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 92.0",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 93.0",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 94.0",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 95.0",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 96.0",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 97.0",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 98.0",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 99.1",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 100.1",
    "now drop rate": " 5.6%"
  },
  {
    "drop rate": " 5.5%",
    "delay": " 101.6"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 9.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 10.1",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 33.2",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 34.2",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 35.2",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 36.2",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 37.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 38.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 39.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 40.2",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 41.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 42.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 43.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 44.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 45.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 46.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 47.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 48.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 49.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 50.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 51.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 52.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 53.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 54.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 55.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 56.3",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 57.3",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 58.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 59.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 60.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 61.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 62.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 63.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 64.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 65.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 66.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 67.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 68.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 69.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 70.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 71.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 72.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 73.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 74.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 75.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 76.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 77.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 78.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 79.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 80.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 81.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 82.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 83.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 84.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 85.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 86.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 87.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 88.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 89.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 90.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 91.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 92.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 93.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 94.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 95.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 96.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 97.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 98.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 99.4",
    "now drop rate": " 2.1%"
  },
  {
    "drop rate": " 2.0%",
    "delay": " 102.8"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 25.6",
    "now drop rate": " 13.3%"
  },
  {
    "time": " 26.6",
    "now drop rate": " 16.5%"
  },
  {
    "time": " 27.7",
    "now drop rate": " 16.0%"
  },
  {
    "time": " 28.7",
    "now drop rate": " 15.4%"
  },
  {
    "time": " 29.7",
    "now drop rate": " 14.9%"
  },
  {
    "time": " 30.7",
    "now drop rate": " 14.5%"
  },
  {
    "time": " 31.7",
    "now drop rate": " 14.1%"
  },
  {
    "time": " 32.7",
    "now drop rate": " 13.8%"
  },
  {
    "time": " 33.7",
    "now drop rate": " 13.5%"
  },
  {
    "time": " 34.7",
    "now drop rate": " 13.2%"
  },
  {
    "time": " 35.7",
    "now drop rate": " 12.8%"
  },
  {
    "time": " 36.7",
    "now drop rate": " 12.5%"
  },
  {
    "time": " 37.7",
    "now drop rate": " 12.2%"
  },
  {
    "time": " 38.7",
    "now drop rate": " 11.9%"
  },
  {
    "time": " 39.7",
    "now drop rate": " 11.6%"
  },
  {
    "time": " 40.7",
    "now drop rate": " 11.4%"
  },
  {
    "time": " 41.7",
    "now drop rate": " 11.2%"
  },
  {
    "time": " 42.7",
    "now drop rate": " 11.0%"
  },
  {
    "time": " 43.7",
    "now drop rate": " 10.8%"
  },
  {
    "time": " 44.7",
    "now drop rate": " 10.6%"
  },
  {
    "time": " 45.7",
    "now drop rate": " 10.4%"
  },
  {
    "time": " 46.7",
    "now drop rate": " 10.2%"
  },
  {
    "time": " 47.8",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 48.8",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 49.8",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 50.8",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 51.8",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 52.8",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 53.8",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 54.8",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 55.8",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 56.8",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 57.8",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 58.8",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 59.8",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 60.8",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 61.8",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 62.8",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 63.8",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 64.8",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 65.8",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 66.8",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 67.8",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 68.8",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 69.8",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 70.8",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 71.8",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 72.9",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 73.9",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 74.9",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 75.9",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 76.9",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 77.9",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 78.9",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 79.9",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 80.9",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 81.9",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 82.9",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 83.9",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 84.9",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 85.9",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 86.9",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 87.9",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 88.9",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 89.9",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 90.9",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 91.9",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 92.9",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 93.9",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 94.9",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 96.0",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 97.0",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 98.0",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 99.0",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 100.0",
    "now drop rate": " 5.5%"
  },
  {
    "drop rate": " 5.4%",
    "delay": " 101.7"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 10.2%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 25.6",
    "now drop rate": " 13.5%"
  },
  {
    "time": " 26.6",
    "now drop rate": " 16.5%"
  },
  {
    "time": " 27.6",
    "now drop rate": " 16.0%"
  },
  {
    "time": " 28.6",
    "now drop rate": " 15.5%"
  },
  {
    "time": " 29.6",
    "now drop rate": " 15.0%"
  },
  {
    "time": " 30.6",
    "now drop rate": " 14.5%"
  },
  {
    "time": " 31.6",
    "now drop rate": " 14.1%"
  },
  {
    "time": " 32.6",
    "now drop rate": " 13.8%"
  },
  {
    "time": " 33.6",
    "now drop rate": " 13.5%"
  },
  {
    "time": " 34.6",
    "now drop rate": " 13.2%"
  },
  {
    "time": " 35.6",
    "now drop rate": " 12.8%"
  },
  {
    "time": " 36.7",
    "now drop rate": " 12.6%"
  },
  {
    "time": " 37.7",
    "now drop rate": " 12.3%"
  },
  {
    "time": " 38.7",
    "now drop rate": " 12.0%"
  },
  {
    "time": " 39.7",
    "now drop rate": " 11.6%"
  },
  {
    "time": " 40.7",
    "now drop rate": " 11.4%"
  },
  {
    "time": " 41.7",
    "now drop rate": " 11.2%"
  },
  {
    "time": " 42.7",
    "now drop rate": " 11.0%"
  },
  {
    "time": " 43.7",
    "now drop rate": " 10.8%"
  },
  {
    "time": " 44.7",
    "now drop rate": " 10.6%"
  },
  {
    "time": " 45.7",
    "now drop rate": " 10.4%"
  },
  {
    "time": " 46.7",
    "now drop rate": " 10.2%"
  },
  {
    "time": " 47.7",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 48.7",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 49.7",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 50.8",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 51.8",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 52.8",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 53.8",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 54.8",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 55.8",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 56.8",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 57.8",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 58.8",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 59.8",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 60.8",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 61.8",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 62.8",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 63.8",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 64.8",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 65.8",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 66.8",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 67.8",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 68.8",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 69.8",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 70.8",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 71.9",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 72.9",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 73.9",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 74.9",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 75.9",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 76.9",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 77.9",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 78.9",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 79.9",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 80.9",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 81.9",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 82.9",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 83.9",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 84.9",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 85.9",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 86.9",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 87.9",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 88.9",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 90.0",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 91.0",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 92.0",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 93.0",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 94.0",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 95.0",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 96.0",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 97.0",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 98.0",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 99.0",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 100.0",
    "now drop rate": " 5.6%"
  },
  {
    "drop rate": " 5.5%",
    "delay": " 102.6"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 25.6",
    "now drop rate": " 13.5%"
  },
  {
    "time": " 26.6",
    "now drop rate": " 16.5%"
  },
  {
    "time": " 27.6",
    "now drop rate": " 15.9%"
  },
  {
    "time": " 28.6",
    "now drop rate": " 15.4%"
  },
  {
    "time": " 29.6",
    "now drop rate": " 14.9%"
  },
  {
    "time": " 30.6",
    "now drop rate": " 14.5%"
  },
  {
    "time": " 31.6",
    "now drop rate": " 14.1%"
  },
  {
    "time": " 32.6",
    "now drop rate": " 13.8%"
  },
  {
    "time": " 33.6",
    "now drop rate": " 13.5%"
  },
  {
    "time": " 34.6",
    "now drop rate": " 13.1%"
  },
  {
    "time": " 35.6",
    "now drop rate": " 12.8%"
  },
  {
    "time": " 36.6",
    "now drop rate": " 12.5%"
  },
  {
    "time": " 37.6",
    "now drop rate": " 12.2%"
  },
  {
    "time": " 38.6",
    "now drop rate": " 11.9%"
  },
  {
    "time": " 39.6",
    "now drop rate": " 11.6%"
  },
  {
    "time": " 40.7",
    "now drop rate": " 11.4%"
  },
  {
    "time": " 41.7",
    "now drop rate": " 11.2%"
  },
  {
    "time": " 42.7",
    "now drop rate": " 11.0%"
  },
  {
    "time": " 43.7",
    "now drop rate": " 10.7%"
  },
  {
    "time": " 44.7",
    "now drop rate": " 10.5%"
  },
  {
    "time": " 45.7",
    "now drop rate": " 10.3%"
  },
  {
    "time": " 46.7",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 47.7",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 48.7",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 49.7",
    "now drop rate": " 9.6%"
  },
  {
    "time": " 50.7",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 51.7",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 52.7",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 53.7",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 54.7",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 55.7",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 56.7",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 57.7",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 58.7",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 59.7",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 60.7",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 61.7",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 62.7",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 63.7",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 64.7",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 65.8",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 66.8",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 67.8",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 68.8",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 69.8",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 70.8",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 71.8",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 72.8",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 73.8",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 74.8",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 75.8",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 76.8",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 77.8",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 78.8",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 79.8",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 80.8",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 81.8",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 82.8",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 83.8",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 84.8",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 85.8",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 86.9",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 87.9",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 88.9",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 89.9",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 90.9",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 91.9",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 92.9",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 93.9",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 94.9",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 95.9",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 96.9",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 97.9",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 98.9",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 99.9",
    "now drop rate": " 5.5%"
  },
  {
    "drop rate": " 5.5%",
    "delay": " 101.9"
  }
]
    ],
    "n=5": [
[
  {
    "time": " 1.0",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 7.1",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 8.1",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 9.1",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 10.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 27.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 28.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 29.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 30.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 31.2",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 32.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 33.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 34.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 35.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 36.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 37.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 38.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 39.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 40.2",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 41.2",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 42.2",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 43.2",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 44.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 45.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 46.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 47.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 48.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 49.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 50.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 51.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 52.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 53.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 54.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 55.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 56.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 57.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 58.3",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 59.3",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 60.3",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 61.3",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 62.3",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 63.3",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 64.3",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 65.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 66.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 67.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 68.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 69.4",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 70.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 71.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 72.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 73.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 74.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 75.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 76.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 77.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 78.4",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 79.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 80.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 81.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 82.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 83.4",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 84.4",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 85.4",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 86.4",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 87.4",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 88.4",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 89.4",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 90.4",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 91.5",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 92.5",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 93.5",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 94.5",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 95.5",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 96.5",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 97.5",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 98.5",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 99.5",
    "now drop rate": " 1.9%"
  },
  {
    "drop rate": " 1.8%",
    "delay": " 111.6"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 30.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 31.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 32.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 33.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 34.2",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 35.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 36.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 37.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 38.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 39.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 40.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 41.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 42.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 43.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 44.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 45.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 46.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 47.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 48.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 49.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 50.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 51.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 52.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 53.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 54.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 55.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 56.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 57.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 58.3",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 59.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 60.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 61.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 62.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 63.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 64.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 65.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 66.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 67.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 68.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 69.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 70.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 71.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 72.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 73.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 74.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 75.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 76.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 77.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 78.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 79.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 80.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 81.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 82.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 83.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 84.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 85.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 86.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 87.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 88.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 89.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 90.4",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 91.5",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 92.5",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 93.5",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 94.5",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 95.5",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 96.5",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 97.5",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 98.5",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 99.5",
    "now drop rate": " 2.1%"
  },
  {
    "drop rate": " 2.0%",
    "delay": " 112.1"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 33.1",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 34.1",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 35.2",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 36.2",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 37.2",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 38.2",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 39.2",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 40.2",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 41.2",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 42.2",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 43.2",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 44.2",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 45.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 46.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 47.2",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 48.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 49.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 50.2",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 51.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 52.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 53.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 54.3",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 55.3",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 56.3",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 57.3",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 58.3",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 59.3",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 60.3",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 61.3",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 62.3",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 63.3",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 64.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 65.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 66.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 67.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 68.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 69.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 70.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 71.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 72.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 73.3",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 74.4",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 75.4",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 76.4",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 77.4",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 78.4",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 79.4",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 80.4",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 81.4",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 82.4",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 83.4",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 84.4",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 85.4",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 86.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 87.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 88.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 89.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 90.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 91.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 92.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 93.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 94.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 95.4",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 96.4",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 97.5",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 98.5",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 99.5",
    "now drop rate": " 2.3%"
  },
  {
    "drop rate": " 2.2%",
    "delay": " 112.1"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 10.4%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 26.8",
    "now drop rate": " 16.6%"
  },
  {
    "time": " 27.8",
    "now drop rate": " 16.1%"
  },
  {
    "time": " 28.8",
    "now drop rate": " 15.6%"
  },
  {
    "time": " 29.8",
    "now drop rate": " 15.1%"
  },
  {
    "time": " 30.8",
    "now drop rate": " 14.7%"
  },
  {
    "time": " 31.8",
    "now drop rate": " 14.3%"
  },
  {
    "time": " 32.8",
    "now drop rate": " 13.9%"
  },
  {
    "time": " 33.8",
    "now drop rate": " 13.8%"
  },
  {
    "time": " 34.8",
    "now drop rate": " 13.4%"
  },
  {
    "time": " 35.8",
    "now drop rate": " 13.0%"
  },
  {
    "time": " 36.9",
    "now drop rate": " 12.7%"
  },
  {
    "time": " 37.9",
    "now drop rate": " 12.4%"
  },
  {
    "time": " 38.9",
    "now drop rate": " 12.1%"
  },
  {
    "time": " 39.9",
    "now drop rate": " 11.8%"
  },
  {
    "time": " 40.9",
    "now drop rate": " 11.6%"
  },
  {
    "time": " 41.9",
    "now drop rate": " 11.4%"
  },
  {
    "time": " 42.9",
    "now drop rate": " 11.1%"
  },
  {
    "time": " 43.9",
    "now drop rate": " 10.9%"
  },
  {
    "time": " 44.9",
    "now drop rate": " 10.7%"
  },
  {
    "time": " 45.9",
    "now drop rate": " 10.5%"
  },
  {
    "time": " 46.9",
    "now drop rate": " 10.3%"
  },
  {
    "time": " 47.9",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 48.9",
    "now drop rate": " 9.9%"
  },
  {
    "time": " 49.9",
    "now drop rate": " 9.8%"
  },
  {
    "time": " 50.9",
    "now drop rate": " 9.6%"
  },
  {
    "time": " 51.9",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 52.9",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 53.9",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 54.9",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 55.9",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 57.0",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 58.0",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 59.0",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 60.0",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 61.0",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 62.0",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 63.0",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 64.0",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 65.0",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 66.0",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 67.0",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 68.0",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 69.0",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 70.0",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 72.2",
    "now drop rate": " 10.0%"
  },
  {
    "time": " 73.2",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 74.2",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 75.2",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 76.2",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 77.2",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 78.2",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 79.2",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 80.2",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 81.2",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 82.2",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 83.2",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 84.2",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 85.2",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 86.2",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 87.3",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 88.3",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 89.3",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 90.3",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 91.3",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 92.3",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 93.3",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 94.3",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 95.3",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 96.3",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 97.3",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 98.3",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 99.3",
    "now drop rate": " 6.9%"
  },
  {
    "drop rate": " 6.8%",
    "delay": " 115.0"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 8.1",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 9.1",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 10.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 26.7",
    "now drop rate": " 17.1%"
  },
  {
    "time": " 27.7",
    "now drop rate": " 16.7%"
  },
  {
    "time": " 28.7",
    "now drop rate": " 16.2%"
  },
  {
    "time": " 29.7",
    "now drop rate": " 15.6%"
  },
  {
    "time": " 30.7",
    "now drop rate": " 15.2%"
  },
  {
    "time": " 31.7",
    "now drop rate": " 14.9%"
  },
  {
    "time": " 32.7",
    "now drop rate": " 14.6%"
  },
  {
    "time": " 33.7",
    "now drop rate": " 14.4%"
  },
  {
    "time": " 34.7",
    "now drop rate": " 14.1%"
  },
  {
    "time": " 35.7",
    "now drop rate": " 13.6%"
  },
  {
    "time": " 36.7",
    "now drop rate": " 13.3%"
  },
  {
    "time": " 37.8",
    "now drop rate": " 13.0%"
  },
  {
    "time": " 38.8",
    "now drop rate": " 12.7%"
  },
  {
    "time": " 39.8",
    "now drop rate": " 12.4%"
  },
  {
    "time": " 40.8",
    "now drop rate": " 12.1%"
  },
  {
    "time": " 41.8",
    "now drop rate": " 11.9%"
  },
  {
    "time": " 42.8",
    "now drop rate": " 11.7%"
  },
  {
    "time": " 43.8",
    "now drop rate": " 11.4%"
  },
  {
    "time": " 44.8",
    "now drop rate": " 11.2%"
  },
  {
    "time": " 45.8",
    "now drop rate": " 11.0%"
  },
  {
    "time": " 46.8",
    "now drop rate": " 10.8%"
  },
  {
    "time": " 47.8",
    "now drop rate": " 10.6%"
  },
  {
    "time": " 48.8",
    "now drop rate": " 10.4%"
  },
  {
    "time": " 49.8",
    "now drop rate": " 10.2%"
  },
  {
    "time": " 50.8",
    "now drop rate": " 10.1%"
  },
  {
    "time": " 51.8",
    "now drop rate": " 9.9%"
  },
  {
    "time": " 52.8",
    "now drop rate": " 9.7%"
  },
  {
    "time": " 53.8",
    "now drop rate": " 9.6%"
  },
  {
    "time": " 54.8",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 55.8",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 56.8",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 57.8",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 58.8",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 59.8",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 60.9",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 61.9",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 62.9",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 63.9",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 64.9",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 65.9",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 66.9",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 67.9",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 68.9",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 69.9",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 71.0",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 72.0",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 73.0",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 74.0",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 75.0",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 76.0",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 77.0",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 78.0",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 79.0",
    "now drop rate": " 8.5%"
  },
  {
    "time": " 80.0",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 81.1",
    "now drop rate": " 8.4%"
  },
  {
    "time": " 82.1",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 83.1",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 84.1",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 85.1",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 86.1",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 87.1",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 88.1",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 89.1",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 90.1",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 91.1",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 92.1",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 93.1",
    "now drop rate": " 7.5%"
  },
  {
    "time": " 94.1",
    "now drop rate": " 7.4%"
  },
  {
    "time": " 95.1",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 96.1",
    "now drop rate": " 7.3%"
  },
  {
    "time": " 97.1",
    "now drop rate": " 7.2%"
  },
  {
    "time": " 98.1",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 99.1",
    "now drop rate": " 7.1%"
  },
  {
    "drop rate": " 6.9%",
    "delay": " 115.1"
  }
]
    ],
    "ospf": [
[
  {
    "time": " 1.0",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 13.0",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 14.0",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.6%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 33.1",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 34.3",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 35.3",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 36.3",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 37.3",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 38.3",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 39.3",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 40.3",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 41.3",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 42.3",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 43.3",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 44.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 45.4",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 46.4",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 47.4",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 49.0",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 50.0",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 51.0",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 52.0",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 53.0",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 54.0",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 55.0",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 56.0",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 57.0",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 58.0",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 59.0",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 60.0",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 61.0",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 62.1",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 63.1",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 64.1",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 65.1",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 66.1",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 67.1",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 68.1",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 69.1",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 70.9",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 71.9",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 73.1",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 74.1",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 75.1",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 76.1",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 77.1",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 78.1",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 79.1",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 80.1",
    "now drop rate": " 5.7%"
  },
  {
    "time": " 81.1",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 82.1",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 83.1",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 84.2",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 85.2",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 86.4",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 87.4",
    "now drop rate": " 7.1%"
  },
  {
    "time": " 88.4",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 89.4",
    "now drop rate": " 7.0%"
  },
  {
    "time": " 90.4",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 91.4",
    "now drop rate": " 6.9%"
  },
  {
    "time": " 92.4",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 93.4",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 94.4",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 95.5",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 96.5",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 97.5",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 98.5",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 99.5",
    "now drop rate": " 6.4%"
  },
  {
    "drop rate": " 6.3%",
    "delay": " 90.3"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 7.6%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 33.1",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 34.4",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 35.4",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 36.4",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 37.4",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 38.4",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 39.4",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 40.4",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 41.4",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 42.4",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 43.4",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 44.4",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 45.4",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 46.4",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 47.4",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 49.4",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 50.4",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 51.4",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 52.4",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 53.4",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 54.4",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 55.4",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 56.4",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 57.5",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 58.5",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 59.5",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 60.5",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 61.5",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 62.5",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 63.5",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 64.5",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 65.5",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 66.5",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 67.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 68.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 69.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 71.1",
    "now drop rate": " 5.6%"
  },
  {
    "time": " 72.1",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 73.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 74.6",
    "now drop rate": " 8.3%"
  },
  {
    "time": " 75.6",
    "now drop rate": " 8.2%"
  },
  {
    "time": " 76.6",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 77.6",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 78.6",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 79.6",
    "now drop rate": " 8.1%"
  },
  {
    "time": " 80.6",
    "now drop rate": " 8.0%"
  },
  {
    "time": " 81.6",
    "now drop rate": " 7.9%"
  },
  {
    "time": " 82.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 83.6",
    "now drop rate": " 7.8%"
  },
  {
    "time": " 84.6",
    "now drop rate": " 7.7%"
  },
  {
    "time": " 86.5",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 87.5",
    "now drop rate": " 9.6%"
  },
  {
    "time": " 88.5",
    "now drop rate": " 9.5%"
  },
  {
    "time": " 89.5",
    "now drop rate": " 9.4%"
  },
  {
    "time": " 90.5",
    "now drop rate": " 9.3%"
  },
  {
    "time": " 91.5",
    "now drop rate": " 9.2%"
  },
  {
    "time": " 92.5",
    "now drop rate": " 9.1%"
  },
  {
    "time": " 93.5",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 94.5",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 95.5",
    "now drop rate": " 8.9%"
  },
  {
    "time": " 96.5",
    "now drop rate": " 8.8%"
  },
  {
    "time": " 97.5",
    "now drop rate": " 8.7%"
  },
  {
    "time": " 98.5",
    "now drop rate": " 8.6%"
  },
  {
    "time": " 99.5",
    "now drop rate": " 8.6%"
  },
  {
    "drop rate": " 8.5%",
    "delay": " 96.2"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 10.6%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 33.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 34.4",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 35.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 36.4",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 37.4",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 38.4",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 39.4",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 40.4",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 41.4",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 42.4",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 43.4",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 44.4",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 45.4",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 46.4",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 47.4",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 48.4",
    "now drop rate": " 3.3%"
  },
  {
    "time": " 49.4",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 50.4",
    "now drop rate": " 3.2%"
  },
  {
    "time": " 51.4",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 52.4",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 53.4",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 54.4",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 55.4",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 56.4",
    "now drop rate": " 3.0%"
  },
  {
    "time": " 57.4",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 58.4",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 59.4",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 60.4",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 61.4",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 62.4",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 63.5",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 64.5",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 65.5",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 66.5",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 67.5",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 68.5",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 69.5",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 70.5",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 71.5",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 72.5",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 73.5",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 74.5",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 75.5",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 76.5",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 77.5",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 78.5",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 79.5",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 80.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 81.5",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 82.5",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 83.5",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 84.5",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 86.5",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 87.5",
    "now drop rate": " 5.5%"
  },
  {
    "time": " 88.5",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 89.5",
    "now drop rate": " 5.4%"
  },
  {
    "time": " 90.5",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 91.5",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 92.5",
    "now drop rate": " 5.3%"
  },
  {
    "time": " 93.5",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 94.5",
    "now drop rate": " 5.2%"
  },
  {
    "time": " 95.5",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 96.5",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 97.5",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 98.5",
    "now drop rate": " 5.0%"
  },
  {
    "time": " 99.5",
    "now drop rate": " 5.0%"
  },
  {
    "drop rate": " 4.9%",
    "delay": " 100.6"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 10.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 11.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 12.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 13.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 33.2",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 34.2",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 35.2",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 36.2",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 37.3",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 38.3",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 39.3",
    "now drop rate": " 3.4%"
  },
  {
    "time": " 40.3",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 41.3",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 42.3",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 43.3",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 44.3",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 45.3",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 46.3",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 47.3",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 48.3",
    "now drop rate": " 3.5%"
  },
  {
    "time": " 49.3",
    "now drop rate": " 4.8%"
  },
  {
    "time": " 50.3",
    "now drop rate": " 4.7%"
  },
  {
    "time": " 51.3",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 52.3",
    "now drop rate": " 4.6%"
  },
  {
    "time": " 53.3",
    "now drop rate": " 4.5%"
  },
  {
    "time": " 54.3",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 55.3",
    "now drop rate": " 4.4%"
  },
  {
    "time": " 56.3",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 57.3",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 58.3",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 59.3",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 60.3",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 61.3",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 62.3",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 63.3",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 64.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 65.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 66.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 67.4",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 68.4",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 69.4",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 70.9",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 71.9",
    "now drop rate": " 4.9%"
  },
  {
    "time": " 73.5",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 74.5",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 75.5",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 76.5",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 77.5",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 78.5",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 79.5",
    "now drop rate": " 6.8%"
  },
  {
    "time": " 80.5",
    "now drop rate": " 6.7%"
  },
  {
    "time": " 81.5",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 82.5",
    "now drop rate": " 6.6%"
  },
  {
    "time": " 83.5",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 84.5",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 85.5",
    "now drop rate": " 6.5%"
  },
  {
    "time": " 86.5",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 87.5",
    "now drop rate": " 6.4%"
  },
  {
    "time": " 88.5",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 89.5",
    "now drop rate": " 6.3%"
  },
  {
    "time": " 90.5",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 91.5",
    "now drop rate": " 6.2%"
  },
  {
    "time": " 92.5",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 93.5",
    "now drop rate": " 6.1%"
  },
  {
    "time": " 94.5",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 95.5",
    "now drop rate": " 6.0%"
  },
  {
    "time": " 96.5",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 97.5",
    "now drop rate": " 5.9%"
  },
  {
    "time": " 98.6",
    "now drop rate": " 5.8%"
  },
  {
    "time": " 99.6",
    "now drop rate": " 5.8%"
  },
  {
    "drop rate": " 5.7%",
    "delay": " 95.8"
  }
],
[
  {
    "time": " 1.0",
    "now drop rate": " 9.0%"
  },
  {
    "time": " 2.0",
    "now drop rate": " 5.1%"
  },
  {
    "time": " 3.0",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 4.0",
    "now drop rate": " 3.1%"
  },
  {
    "time": " 5.0",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 6.0",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 7.0",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 8.0",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 9.0",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 10.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 11.0",
    "now drop rate": " 2.1%"
  },
  {
    "time": " 12.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 13.0",
    "now drop rate": " 2.0%"
  },
  {
    "time": " 14.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 15.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 16.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 17.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 18.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 19.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 20.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 21.1",
    "now drop rate": " 1.9%"
  },
  {
    "time": " 22.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 23.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 24.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 25.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 26.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 27.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 28.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 29.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 30.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 31.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 32.1",
    "now drop rate": " 1.8%"
  },
  {
    "time": " 33.1",
    "now drop rate": " 1.7%"
  },
  {
    "time": " 34.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 35.2",
    "now drop rate": " 2.9%"
  },
  {
    "time": " 36.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 37.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 38.2",
    "now drop rate": " 2.8%"
  },
  {
    "time": " 39.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 40.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 41.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 42.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 43.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 44.2",
    "now drop rate": " 2.7%"
  },
  {
    "time": " 45.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 46.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 47.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 48.2",
    "now drop rate": " 2.6%"
  },
  {
    "time": " 49.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 50.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 51.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 52.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 53.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 54.2",
    "now drop rate": " 2.5%"
  },
  {
    "time": " 55.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 56.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 57.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 58.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 59.3",
    "now drop rate": " 2.4%"
  },
  {
    "time": " 60.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 61.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 62.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 63.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 64.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 65.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 66.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 67.3",
    "now drop rate": " 2.3%"
  },
  {
    "time": " 68.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 69.3",
    "now drop rate": " 2.2%"
  },
  {
    "time": " 70.4",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 71.4",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 72.4",
    "now drop rate": " 4.3%"
  },
  {
    "time": " 73.4",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 74.4",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 75.4",
    "now drop rate": " 4.2%"
  },
  {
    "time": " 76.4",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 77.4",
    "now drop rate": " 4.1%"
  },
  {
    "time": " 78.4",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 79.4",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 80.4",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 81.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 82.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 83.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 84.4",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 85.5",
    "now drop rate": " 4.0%"
  },
  {
    "time": " 86.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 87.5",
    "now drop rate": " 3.9%"
  },
  {
    "time": " 88.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 89.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 90.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 91.5",
    "now drop rate": " 3.8%"
  },
  {
    "time": " 92.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 93.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 94.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 95.5",
    "now drop rate": " 3.7%"
  },
  {
    "time": " 96.5",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 97.5",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 98.5",
    "now drop rate": " 3.6%"
  },
  {
    "time": " 99.5",
    "now drop rate": " 3.6%"
  },
  {
    "drop rate": " 3.5%",
    "delay": " 101.4"
  }
]
    ]
}

fig, axs = plt.subplots(3, 2, figsize=(9, 12))

fig_cnt = 0
for lofi_n, result in data.items():
    if lofi_n == "n=0":
        continue
    
    ax = axs[fig_cnt // 2, fig_cnt % 2]

    title = f'66 satellites, 5% failure, {lofi_n}'
    ax.set_title(title)

    ax.set_xlim(0, 100)
    ax.set_xlabel('time (s)')

    ax.set_ylim(0, 25)
    ax.set_ylabel('drop rate')
    # yticks = [0, 10, 20]
    # ax.set_yticks(yticks)
    # ax.set_yticklabels([f'{y: d}' for y in yticks])
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())

    ax.grid(True)

    for i, data in enumerate(result):
        time_points = [float(d['time'].strip()) for d in data[:-1]]
        drop_rates = [float(d['now drop rate'].strip('%')) for d in data[:-1]]
        ax.plot(time_points, drop_rates, label=f"test{i + 1}")

    
    # legend = ax.get_legend()
    # if legend:
    #     legend.texts[0].set_linespacing(0.25)
    ax.legend(fontsize=8)    
    fig_cnt += 1

plt.subplots_adjust(hspace=0.6, wspace=0.4)

plt.show()