def main():
    import time
    import pandas as pd
    import numpy as np
    from datetime import datetime

    
    # determines the list of eligible inputs the user can select from for the application filter criteria
    CITY_DATA = { 'chicago': 'chicago.csv',
                  'new york': 'new_york_city.csv',
                  'washington': 'washington.csv' }

    CITIES = ['chicago', 'new york', 'washington']

    FILTERS = ['month', 'day', 'both', 'none']
    
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    print("Hello! Let's explore some US Bikeshare data!") 
    
    # create global var df
    df = ""
    
    # determines the time the application starts running. In this case the clock is starting from the moment the user sees the the welcome message. This is used to calculate the amount of time the application has been taking to run throughout various points later in the application.
    start_time = time.time() # global var
    
    # collects the user input allowing the application to filter based on the criteria including city, timescale, month or day 
    def get_filters():
        global df # to update value to global df
        while True:
            city = input('Would you like to see the data for Chicago, New York or Washington? \n> ').lower()

            # only breaks when users type in right city name
            if city in CITIES:
                break
            else:
                print("oops, wrong city name")
        filter_type = ''
        while True:         
            # input from user determines whether application will filter by month, day, both or neither
               filter_type = input('Would you like to filter by month, day, both or not at all? Type "none" for no time filter \n> ').lower()
               if filter_type in FILTERS:
                   break
               else:
                   print("oops, that doesn't look right")
        month = 'all'
        
        # get user input for month (all, january, february, ... , june)
        while (filter_type == 'month' or filter_type == "both"):         
            
               month = input('Which month? January, February, March, April, May or June? \n '\
               '> You can type \'all\' again to apply no month filter. ').lower()
               if month in MONTHS:
                   break
               else:
                   print("oops, wrong month name")
        day = 'all'
        
        # get user input for day of the week
        while (filter_type == 'day' or filter_type == "both"):         
               day = input('Which day? \n '\
               '> You can type \'all\' again to apply no day filter. \n(e.g. all, monday, sunday)').lower()
               if day in DAYS:
                   break
               else:
                   print("oops, wrong day number")       


        # reads data from specific csv file based on users input for city filter
        df = pd.read_csv(CITY_DATA[city])

        #converts timestamp to date and time value
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week from Start Time to create new columns. This allows us to filter by month/day
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()

        if month != 'all': # no filter
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1

            df = df[df['month'] == month]


            if day != 'all':
                # filter by day of week to create the new dataframe
                df = df[df['day_of_week'] == day.title()]

        df['Start Time'] = pd.to_datetime(df['Start Time'])

            # extract month and day of week from Start Time to create new columns. This allows us to filter by month/day
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()
       
        
        # function calculates popular travel time statistics
    def popular_travel_times():
        global df        # to update value to global df
        print('\nCalculating The Most Frequent Times of Travel...\n')

            # TO DO: display the most common month
        popular_month = df['month'].mode()
        print('Most Popular Month:', popular_month)

            # TO DO: display the most common day of week
        popular_day = df['day_of_week'].mode()[0] # [0] - access Value
        print('Most Popular Day of Week:', popular_day)

            # TO DO: display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        popular_hour = df['hour'].mode()[0]
        print('Most Popular Start Hour:', popular_hour)
            # shift + tab

        print("count: " + str(len(df[df['hour'] == popular_hour])))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
        

    # function calculates station statistics
    def station_stats():
        global df # to update value to global df
        """Displays statistics on the most popular stations and trip."""

        print('\nCalculating The Average Trip Duration...\n')
        #start_time= time.time()

        #df['total_duration'] = df['End Time'] - df['Start Time']

        print(float(df['Trip Duration'].sum()))
        #print("Total Duration:", total_duration)   
        #df['Val_Diff'] = df['Val10'] - df['Val1']

        total_duration_count = df['Trip Duration'].count()
        print("Count: ", total_duration_count)

        average_duration = df['Trip Duration'].mean()
        print("Avg Duration:", average_duration)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

        # TO  DO: display most commonly used start station
        print('\nCalculating The Most Popular Start and End Stations...\n')

        popular_start_station = df['Start Station'].mode()[0] # [0] - access Value
        print('Most Popular Start Station:', popular_start_station)

        count_of_start_station = df['Start Station'].value_counts().max()
        print("Count: ", count_of_start_station)

        popular_end_station = df['End Station'].mode()[0] #        
        print('Most Popular End Station:', popular_end_station)
        
        count_of_end_station = df['End Station'].value_counts().max()
        print("Count: ", count_of_end_station)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
        # function calculates popular travel route statistics
    def popular_trip_data():
        global df # to update value to global df
        print('\nCalculating The Most Popular Trip...\n')

        print('Most Popular Trip:')
        
        count_of_occurences = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
        counts = df.groupby(['Start Station','End Station']).size().idxmax()
        #print(counts[0].iloc[0])
        print('Trip: ', str(counts), ', Count:' + str(count_of_occurences.iloc[0]))
        print('-'*40)

        # function calculates user statistics
    def user_data():
        global df # to update value to global df
        print('\nCalculating User Type...\n')

        subscriber = df['User Type'].value_counts().Subscriber
        print('Subscribers: ', subscriber)

        customer = df['User Type'].value_counts().Customer
        print('Customers: ', customer)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

        print('\nCalculating The Next Statistic...Gender\n')
        
        if 'Gender' in df.columns:
            male = df['Gender'].value_counts().Male
            print('Male: ', male)

            female = df['Gender'].value_counts().Female
            print('Female: ', female)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


        print('\nCalculating The Next Statistic...Birth Year\n')

        # get currentYear from Date. the value in csv data is then subtracted to get the age profiles of users. This data does not take day or month of birth into consideration so values below are rounded up/down
        if 'Birth Year' in df.columns:
            current_year = datetime.now().year
            average_user_age = current_year - df['Birth Year'].mode()[0]
            print('Average User Age: ', average_user_age)

            youngest_user = current_year - df['Birth Year'].max()
            print('Youngest User Age: ', youngest_user)

            oldest_user = current_year - df['Birth Year'].min()
            print('Oldest User Age: ', oldest_user)
            
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    
    
        # allows users to see raw data from csv files
    
    
    
    
    # all functions have been defined in main()
    # the first function get_filters() can start from here
    # then run all functions one by one
    get_filters()
    popular_travel_times()
    station_stats()
    popular_trip_data()
    user_data()
   
    
    
    # restarts application
    restart_response = ['yes', 'no']    
    restart = ''   
    while restart not in restart_response:
        print("\nDo you wish to explore more bikeshare data? Enter yes to rerun application")
        restart = input().lower()
        if restart == "yes":
            main()
               
        elif restart not in restart_response:
            print("\nOops that doesn't look right.")
            
        elif restart =="no":
            break
            
main()  
        
