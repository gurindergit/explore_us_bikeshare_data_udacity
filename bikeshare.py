# explore_us_bikeshare_data_udacity
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nFrom which city would you like to explore the data? \n').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('\nData available only for Chicago, New York City & Washington. Please choose. \n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nSelect any month from January to June. \nYou can also select all by writing "all". \n').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('\nIt seems like you selected an unavailable month. Try again. \n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nSelect any day from Monday to Sunday. \nYou can also select all by writing "all". \n').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('\nIt seems like you selected an unavailable day. Try again. \n').lower()


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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month= df['month'].mode()[0]
    months= ['January','February','March','April','May','June']
    month= months[month-1]
    print("The most common month is {}.".format(month))


    # TO DO: display the most common day of week
    day= df['day_of_week'].mode()[0]
    print("The most common day of the week is {}.".format(day))


    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    hour=df['Start Hour'].mode()[0]
    print("The most common start hour is {}:00.".format(hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: ', df['Start Station'].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print('The most commonly used end station is: ', df['End Station'].value_counts().idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    # fc == Most frequent combination of start station and end station trip variable
    fc = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip is \n{}.'.format(fc))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 3600.0
    print('Total travel time is {} hours.'.format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 3600.0
    print('Mean travel time is {} hours.'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print(user_types)
        
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print(gender)
    
    except KeyError:
        print('Gender not available for the selected city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        print('The earliest year of birth is {}.'.format(earliest))
    
        most_recent = int(df['Birth Year'].max())
        print('The most recent year of birth is {}.'.format(most_recent))
    
        most_common = int(df['Birth Year'].mode())
        print('The most common year of birth is {}.'.format(most_common))
        
    except KeyError:
        print('Birth year not available for the selected city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data(df):
    """Display raw data if the user wishes to do so."""
    start = 0
    view_data = input('Would you like to view 5 rows of invidual trip data? Enter yes or no.\n').lower()
    while True:
        if view_data not in ['yes', 'no']:
            print('Invalid input. Try typing "yes" or "no".\n')
        elif view_data == 'yes':
            print(df.iloc[start:start + 5])
            start += 5
        elif view_data == 'no':
            break
        else:
            print('Invalid.')
        view_data = input('Would you like to view 5 rows of invidual trip data? Enter yes or no.\n').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
