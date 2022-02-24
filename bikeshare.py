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
    city = input("Would you like to see data for Chicago, New York city, or Washington? ").lower()
    while city not in CITY_DATA: 
        print("Please choose a rihgt city name ")
        city = input("Would you like to see data for Chicago, New York city, or Washington? ").lower()
        
    # TO DO: get user input for month (all,january
    months = ["january", "february", "march", "april", "may", "june", "all"]
    month = input("Do you want to filter data by month or all? you can choose month from January.... june!  ").lower()
    while month not in months: 
        print("Please enter a valid month or enter all")
        month = input("Do you want to filter data by month or all? you can choose month from January.... june!  ").lower()
   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"] 
    day = input("Do you want to filter data by day or not at all? you can choose month from Monday...Sunday!  ").lower()
    while day not in days: 
        print("Please choose a day or choose all ")
        day = input("Do you want to filter data by day or not at all? you can choose month from Monday...Sunday!   ").lower()
    
    
    
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = (months.index(month) + 1)
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   
    return df


def time_stats(df):
    
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df.mode()['month'][0]
    print('\nMost common month:', most_common_month )


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    most_common_day = df.mode()['day'][0]
    print('\nMost common day of week:', most_common_day )
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df.mode()['hour'][0]
    print('\nMost common start hour:', most_common_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station1 = df.mode()['Start Station'][0]
    print('\nMost commonly used start station :', common_station1 )
    


    # TO DO: display most commonly used end station
    common_station2 = df.mode()['End Station'][0]
    print('\nMost commonly used end station :', common_station2 )
    


    # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('\nMost frequent combination of start station and end station trip :', combination  )
    """Helped by Stack Overflow"""


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time : ' , (total_travel_time / 60))


    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time : ' , avg_travel_time)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
   
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCounts of user types\n' , user_types)


    # TO DO: Display counts of gender 
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('\nCounts of gender\n' , gender_count)
        
   
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print('\nEarliest year of birth :' , earliest)
        
        recent = df['Birth Year'].max()
        print('\nMost recent year of birth :' , recent)
        
        common = df.mode()['Birth Year'][0]
        print('\nMost Common year of birth :' , common)

 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw_data(df):
    """Helped by Stack Overflow"""
    n = 0
    while True:
        answer = input('\nWould you like to have a look on some raw data? Enter yes or no:\n ')
        if answer.lower() == 'yes':
            print(df.iloc[n:n+5, :])
            n += 5
        else:
            break
    
    
            
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
