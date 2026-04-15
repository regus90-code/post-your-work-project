# yes I did write this code

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Please enter a valid city (Chicago, New York City, or Washington): ").lower()

    # get user input for month (all, january, february, ... , june)

    month = input("Which month? (all, january, february, march, april, may, june) ").lower()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        month = input("Please enter a valid month: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Which day? (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) ").lower()
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
        day = input("Please enter a valid day: ").lower()

    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if 'month' in df.columns:
        common_month = df['month'].mode()[0]
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        print('Most Common Month:', months[common_month - 1])

    # display the most common day of week
    if 'day_of_week' in df.columns:
        common_day = df['day_of_week'].mode()[0]
        print('Most Common Day of Week:', common_day)

    # display the most common start hour
    if 'hour' in df.columns:
        common_hour = df['hour'].mode()[0]
        print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    if 'Start Station' in df.columns:
        common_start = df['Start Station'].mode()[0]
        print('Most Commonly Used Start Station:', common_start)

    # display most commonly used end station
    if 'End Station' in df.columns:
        common_end = df['End Station'].mode()[0]
        print('Most Commonly Used End Station:', common_end)

    # display most frequent combination of start station and end station trip
    if 'Start Station' in df.columns and 'End Station' in df.columns:
        combination = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
        print('Most Frequent Trip:', combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    if 'Trip Duration' in df.columns:
        total_time = df['Trip Duration'].sum()
        print('Total Travel Time:', total_time, 'seconds')

    # display mean travel time
    if 'Trip Duration' in df.columns:
        mean_time = df['Trip Duration'].mean()
        print('Mean Travel Time:', mean_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print('Counts of User Types:')
        print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(gender_counts)
    else:
        print('\nGender data not available for this city.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print('\nEarliest Year of Birth:', earliest)
        print('Most Recent Year of Birth:', most_recent)
        print('Most Common Year of Birth:', most_common)
    else:
        print('\nBirth Year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
