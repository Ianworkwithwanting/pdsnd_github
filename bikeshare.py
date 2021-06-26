import time
import pandas as pd
import numpy as np
# for project
#for step 4
# for step 4 -2  
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
citys = ['chicago','new york city' , 'washington']
months = ['all','january','february','march','april','may','june']
days=['all','monday','tuesday','wendesday','thursday','friday','saturday','sunday']
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
    city=input('Please input for the travel city: ').lower()
    while city not in citys :
        print('Pls type chicago or new york city or washington')
        city=input('Please input for the travel city: ').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month =input('Please type the month: ').lower()
    while month not in months :
         print('Pls type all,january,february,march,april,may,june')
         month =input('Please type the month: ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =input('Please type the day: ').lower()
    while day not in days :
        print('Pls type all,monday,tuesday,wendesday,thursday,friday,saturday,sunday')
        day =input('Please type the day: ').lower()
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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])

    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name

    if month != 'all' :
      H_month =['january','february','march','april','may','june']
      month=H_month.index(month)+1
      df = df[df['month'] == month]

    if day != 'all' :
      df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour']=df['Start Time'].dt.hour
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('the common travel month is :',popular_month )
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('the common travel day is :',popular_day )
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('the common travel start hour is :',popular_hour )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most commonly start station is : ', common_start )
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most commonly end station is : ', common_end )
    # TO DO: display most frequent combination of start station and end station trip
    df['Fre Station']=df['Start Station']+' - '+ df['End Station']
    common_sta = df['Fre Station'].mode()[0]
    print('The most common start-end station is :',common_sta)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is :',Total_travel_time)

    # TO DO: display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is :',Mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('Counts of user types :',user_types)
    # TO DO: Display counts of gender
    try :
       Gender=df['Gender'].value_counts()
       print('Counts of gender :',Gender)
    # TO DO: Display earliest, most recent, and most common year of birth
       Yongest = df['Birth Year'].max()
       oldest = df['Birth Year'].min()
       common_year=df['Birth Year'].mode()
       print('the recent year is : ', Yongest)
       print('the earlist year is : ', oldest)
       print('the most coomon year is : ', common_year)
    except KeyError:
       print('There is no gender and birth day data in that city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def row_data(df) :
    display_data=input('Do you want to see 5 rows of data,Yes or No\n').lower()
    start_loc = 0
    while display_data == 'yes':
        start_loc+=5
        print(df.iloc[:start_loc])
        display_data = input('Do you also want to see next 5 rows ?, Yes or No\n ').lower()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
