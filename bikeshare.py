import time
import pandas as pd
import numpy as np

CITY = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY:
        city_name = input("\nWhat is the name of the city (E.g. Input either chicago, new york city, washington)\n")
        if city_name.lower() in CITY:
            #We were able to get the name of the city to analyze data.
            city = CITY[city_name.lower()]
        else:
            #We were not able to get the name of the city to analyze data so we continue the loop.
            print("Sorry the city name is not valid to analyze data, Please input either chicago, new york city or washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH:
        month_name = input("\nPlease choose the month to filter data? (E.g. Input either 'all' to apply no month filter or january, february, march, april, may, june)\n")
        if month_name.lower() in MONTH:
            #We were able to get the name of the month to analyze data.
            month = month_name.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry the month name is not valid to filter data, Please input either 'all' to apply no month filter orjan, feb, mar, apr, may, jun.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY:
        day_name = input("\nWhat is the name of the day to filter data? (E.g. Input either 'all' to apply no day filter or monday, tuesday, wednesday, thursday, friday, saturday, sunday.)\n")
        if day_name.lower() in DAY:
            #We were able to get the name of the month to analyze data.
            day = day_name.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry the month name is not valid to filter data, Please input either 'all' to apply no day filter or monday, tuesday, wednesday, thu, fri, sat, sun.\n")

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
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is " + MONTH[common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is " + common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
        # display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    # display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    # display most frequent combination of start station and end station trip
    df['combination_station'] = df['Start Station'] + df['End Station']
    frequent_combination = df['combination_station'].mode()[0]

    print('The most popular start station is '  +str(common_start_station))
    print('The most popular end station is ' + str(common_end_station))
    print('The most frequent station trip is '  +str(frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    t_travel = (df['Trip Duration'].sum()) /60
    # display mean travel time
    m_travel = (df['Trip Duration'].mean())/60
    print('Total travel time: '  +str(t_travel))
    print('Mean travel time'  +str(m_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usr_tp = df['User Type'].value_counts()
    print("The count of user types is \n" + str(usr_tp))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("\nThe count of user gender is \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        ea_birth = df['Birth Year'].min()
        rc_birth = df['Birth Year'].max()
        cm_birth = df['Birth Year'].mode()[0]
        print('\nEarliest birth  is; {}'.format(ea_birth))
        print('Most recent birth is {}'.format(rc_birth))
        print('Most common birth  is {}'.format(cm_birth) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    nx = 0
    while True:
        five_raw_data = input('\nDo you want to view next five row of raw data? Enter y or n.\n')
        if five_raw_data.lower() != 'y':
            return
        nx = nx + 5
        print(df.iloc[nx:nx+5])

#main function part
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
