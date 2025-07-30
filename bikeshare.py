import time
import pandas as pd
import numpy as np

 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

 
def get_filters():
    """
    Asks user to specify a city, month, or a day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (1 for Chicago, 2 for New York City, 3 for Washington)
    print()
    city = ''
    while city not in ['1', '2', '3']:
        city = input('Enter city (1 for Chicago, 2 for New York City, 3 for Washington): ')
        if city not in ['1', '2', '3']:
            print('Invalid city selection. Please enter 1, 2, or 3.')
    city = {'1': 'chicago', '2': 'new york city', '3': 'washington'}.get(city)
    print()

# this project rocks
# All your base are belong to us
 
    # get user input for month (1-6 for january-june, 7 for all)
    month = ''
    while month not in ['1', '2', '3', '4', '5', '6', '7']:
        month = input('Enter month (1 for January, 2 for February, 3 for March, 4 for April, 5 for May, 6 for June, 7 for All): ')
        if month not in ['1', '2', '3', '4', '5', '6', '7']:
            print('Invalid month selection. Please enter 1-7.')
    month = {'1': 'january', '2': 'february', '3': 'march', '4': 'april', '5': 'may', '6': 'june', '7': 'all'}.get(month)
    print()

 
    # get user input for day of week (1-7 for Monday-Sunday, 8 for all)
    day = ''
    while day not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        day = input('Enter day (1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday, 6 for Saturday, 7 for Sunday, 8 for All): ')
        if day not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print('Invalid day selection. Please enter 1-8.')
    day = {'1': 'monday', '2': 'tuesday', '3': 'wednesday', '4': 'thursday', '5': 'friday', '6': 'saturday', '7': 'sunday', '8': 'all'}.get(day)
    print()
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
    # Load data file
    df = pd.read_csv(CITY_DATA[city])
    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month and day of week
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month.title()]
    # Filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

 
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

 
    # display the most common month
    common_month = df['month'].mode()[0]
    print(f'Most common month: {common_month}')


 
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f'Most common day of week: {common_day}')


 
    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_hour = df['start_hour'].mode()[0]
    print(f'Most common start hour: {common_hour}:00')


 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

 
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

 
    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'Most common start station: {common_start_station}')


 
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'Most common end station: {common_end_station}')


 
    # display most frequent combination of start station and end station trip
    combined_stations = df['Start Station'] + ' to ' + df['End Station']
    common_combination = combined_stations.mode()[0]
    print(f'Most common trip: {common_combination}')


 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


 
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

 
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_hours, total_remainder = divmod(total_travel_time, 3600)
    total_minutes, total_seconds = divmod(total_remainder, 60)
    print(f'Total travel time: {int(total_hours)} hours, {int(total_minutes)} minutes, and {int(total_seconds):02d} seconds')


 
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_hours, mean_remainder = divmod(mean_travel_time, 3600)
    mean_minutes, mean_seconds = divmod(mean_remainder, 60)
    print(f'Average travel time: {int(mean_hours)} hours, {int(mean_minutes)} minutes, and {int(mean_seconds):02d} seconds')


 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


 
def user_stats(df):
    """Displays statistics on bikeshare users."""

 
    print('\nCalculating User Stats...\n')
    start_time = time.time()

 
    # Display counts of user types
    try:
        print(f"User Type counts:\n{df['User Type'].value_counts().to_string()}")
        print()
    except KeyError:
        print("User Type data not available for this city.")


 
    # Display counts of gender
    try:
        print(f"Gender counts:\n{df['Gender'].value_counts().to_string()}")
        print()
    except KeyError:
        print("Gender data not available for this city.")


 
    # Display earliest, most recent, and most common year of birth
    try:
        print(f"Earliest birth year: {df['Birth Year'].dropna().astype(int).min()}")
        print(f"Most recent birth year: {df['Birth Year'].dropna().astype(int).max()}")
        print(f"Most common birth year: {df['Birth Year'].dropna().astype(int).mode()[0]}")
    except KeyError:
        print("Birth Year data not available for this city.")


 
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

 
        # Prompt to view raw data
        view_data = input('Would you like to see the raw data? Enter yes or no: ').lower()
        if view_data == 'yes':
            start_idx = 0
            while start_idx < len(df):
                print(df.iloc[start_idx:start_idx+5])
                start_idx += 5
                more = input('Would you like to see 5 more rows? Enter yes or no: ').lower()
                if more != 'yes':
                    break

 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


 
if __name__ == "__main__":
    main()
