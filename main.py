import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

month_data = {"january": 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, "all": 0}
days_data = ["monday", 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', "all"]


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs
    print("To proceed please select a city from the following 'Chicago','New York city','Washington'")
    # while loop to force correct user input and avoid errors "city"
    city_input = 0
    while city_input < 1:
        city = input('city to explore:')
        city = str.lower(city)
        if city in CITY_DATA:
            city_input += 2
        else:
            print("sorry we didn't get your city selection please try again")

    # TO DO: get user input for month (all, january, february, ... , june)
    # while loop to force correct user input and avoid errors "month"
    month_input = 0
    while month_input < 1:
        print("Please select a month from the following: January, February, March, April, May, June,"
              "'for no filter please type All")
        month = input('Month to explore:')
        month = str.lower(month)
        if month in month_data:
            month_input += 2
        else:
            print("sorry we didn't get your month selection please try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_input = 0
    while days_input < 1:
        print("Please select a day from the following: Monday, Tuesday, Wednesday, Thursday, Friday, "
              "Saturday, Sunday "
              "'for no filter please type All")
        day = input("Day to explore:")
        day = str.lower(day)
        if day in days_data:
            days_input += 2
        else:
            print("sorry we didn't get your day selection please try again")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        # "if" function is used to determine city
        if city == "new york city":
            # importing data file based on outcome from the "if" function
            df = pd.read_csv(r"new_york_city.csv")
            # start time to date time
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            # creating month
            df['month'] = df['Start Time'].dt.month
            # creating day
            df['day_of_week'] = df['Start Time'].dt.day_name()
            # "if functions" to act as control flow for user inputs for month/day
            if month != "all":
                df = df[df['month'] == month_data[month]]
            if day != "all":
                df = df[df['day_of_week'] == day.title()]
            return df.dropna()
        elif city == "chicago":
            df = pd.read_csv(r"chicago.csv")
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['month'] = df['Start Time'].dt.month
            df['day_of_week'] = df['Start Time'].dt.day_name()
            if month != "all":
                df = df[df['month'] == month_data[month]]
            if day != "all":
                df = df[df['day_of_week'] == day.title()]
            return df
        elif city == "washington":
            df = pd.read_csv(r"washington.csv")
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['month'] = df['Start Time'].dt.month
            df['day_of_week'] = df['Start Time'].dt.day_name()
            if month != "all":
                df = df[df['month'] == month_data[month]]
            if day != "all":
                df = df[df['day_of_week'] == day.title()]
            return df
    except:
        print("sorry an error was trigger please restart the programme")

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    if common_month == 1:
        print("The most common month is 'january', please note if a specific month was selected it will always \nshow "
              "as most common'")
    elif common_month == 2:
        print("The most common month is 'february', please note if a specific month was selected it will always \nshow"
              " as most common'")
    elif common_month == 3:
        print("The most common month is 'march', please note if a specific month was selected it will always \nshow"
              " as most common'")
    elif common_month == 4:
        print("The most common month is 'april', please note if a specific month was selected it will always \nshow"
              " as most common'")
    elif common_month == 5:
        print("The most common month is 'may', please note if a specific month was selected it will always \nshow"
              " as most common'")
    elif common_month == 6:
        print("The most common month is 'june', please note if a specific month was selected it will always \nshow"
              " as common'")

    # display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print(
        'The most common day is {} , please note if a specific day was selected it will always show as '
        'common'.format(common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is {}".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station is {}".format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station is {}".format(end_station))

    # display most frequent combination of start station and end station trip
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most common trip is {}".format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration_secs = df["Trip Duration"].sum()
    total_duration_minutes = total_duration_secs / 60
    total_duration_hours = total_duration_minutes / 60
    print("Total trip duration in secs:{}".format(total_duration_secs))
    print("Total trip duration in minutes:{}".format(total_duration_minutes))
    print("Total trip duration in minutes:{}".format(total_duration_hours))
    # display mean travel time
    trip_duration_mean = df["Trip Duration"].mean()
    print("Trip duration mean is: {}".format(trip_duration_mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print(user_types[['Subscriber', 'Customer']])
    # Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print(gender_count[["Male", "Female"]])
    except:
        print("'Gender' data is not available for the selected city")
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_date = df["Birth Year"].min()
        most_recent_date = df["Birth Year"].max()
        most_common_year = df["Birth Year"].value_counts().idxmax()
        print(int(earliest_date))
        print(int(most_recent_date))
        print(int(most_common_year))
    except:
        print("'Birth Year' data is not available for the city selected")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_stats(df):
    # user input to load raw data
    print("would you like to see the raw data for your selected city?")
    raw_data_input = ["yes", "no"]
    initial_input = 0
    # while loop to handle errors in input
    while initial_input < 1:
        user_input = str.lower(input('please type Yes or No: '))
        if user_input in raw_data_input:
            initial_input += 2
            while user_input == 'yes':
                print(df.sample(5))
                user_input = str.lower(input("to load more data type 'yes', to quit insert any character: "))

        else:
            print("sorry we didn't get your select please try again")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

