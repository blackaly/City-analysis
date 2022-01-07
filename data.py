import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
'new york city': 'new_york_city.csv',
'washington': 'washington.csv' }
def get_filters():

    while True:
        try:
            name_of_cities = ['Chicago', 'New York', 'Washington']
            city = input("Please, Choose the city that you need to do a nalyze on it: ")
            if city in name_of_cities:
                break
        except ValueError:
            print ("City does not exist !")
            continue
        else:
            break
    while True:
        try:
            months = ['January', 'February', 'March', 'April', 'May',
    'June']


            month = input("Please,which month? January, February, March, April, May, June.")

            if month in months:
                break
        except ValueError:
            print ("Month does not exist !")
            continue
        else:
            break
    while True:
        try:
            days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            day = input("Which day, Sunday, Monday, Tuesday, Wednesday,Thursday, Friday, Saturday: ")
            if day in days:
                break
        except ValueError:
            print ("Day does not exist !")
            continue
        else:
            break
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
# TO DO: get user input for month (all, january, february, ... , june)
# TO DO: get user input for day of week (all, monday, tuesday, ...sunday)

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if a
    pplicable.
    Args:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply
    no month filter
    (str) day - name of the day of week to filter by, or "all" to a
    pply no day filter
    Returns:
    df - Pandas DataFrame containing city data filtered by month an
    d day
    """
    while True:
        try:
            df = pd.read_csv(CITY_DATA[city])
        except ValueError:
            print("There are no country with this name")
            continue
        else:
            break
    df ['Start Time'] = pd.to_datetime(df['Start Time'])
    df ['month'] = df['Start Time'].dt.month
    df ['day_in_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month ]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel..\n')
    start_time = time.time()
# TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is:", common_month)
# TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day is:", common_day_of_week)
# TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common hour is:", common_start_hour,"\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
# TO DO: display most commonly used start station
    common_start_starion = df['Start Station'].mode()[0]
    print("The common Start Station is:", common_start_station)

    common_end_station = df['End Station'].mode()[0]
    print("The common Start Station is:", common_end_station)
# TO DO: display most frequent combination of start station and end station trip
    combination_SE_stations = df.groupby(['Start Station','End Station'
]).size().idxmax()
    print("Most frequent combination of start station and end station trip:",combination_SE_stations)
# We can use df.mode also.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
# TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is:", total_travel_time)
# TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time:",total_travel_time, "\n")
    print("\nThis took %s seconds." % (time.time() -start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
# TO DO: Display counts of user types
    user_types = df['User Types'].value_counts()
    print("The counts of user types is:", user_types)
# TO DO: Display counts of gender
    gender_of_user = df['Gender'].value_counts()
    print("The counts of gender of users is:", gender_of_users)
# TO DO: Display earliest, most recent, and most common year of birth
    year_of_brith = df['Brith Year']
    earliest_brith_year = year_of_brith.min()
    print("The earliest brith year is:", earliest_brith_year,"\n")
    most_recent_year = year_of_brith.mix()
    print("The most recent year is:", most_recent_year,"\n")
    common_year_of_brith = year_of_brith.mode()[0]
    print("The common year of brith is:", common_year_of_brith,"\n")
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
        if restart.lower() != 'yes' | restart.upper() == 'YES' | restart == 'Yes':
            break
if __name__ == "__main__":

    main()
