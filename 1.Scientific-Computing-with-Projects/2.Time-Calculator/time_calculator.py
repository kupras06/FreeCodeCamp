def add_time(start, duration,day = None):
    def swapm(a):
        if a=='PM':  return 'AM'
        return 'PM'
    #print(' Question is : ',start,duration,day)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
    # Extracting time in terms of hour and minutes
    time = start.split()
    time_day = time[1]
    time_hour = time[0].split(':')
    time_min = int(time_hour[1])
    time_hour = int(time_hour[0])
    # Extracting duration time in terms of hour and minutes
    d_hour = duration.split(':')
    d_min = int(d_hour[1])
    d_hour = int(d_hour[0])
    time_min += d_min
     # Converting mins to hours if mins greater than 60
    if time_min>60:
        time_min -= 60
        time_hour+=1
    interval = 0
    # finding number of intervals in terms of days in the given update duration
    # reducig the duration hour to less than 24
    if d_hour > 24:
        interval = d_hour//24
        d_hour %= 24
    # Incrementing time with duration hours
    time_hour += d_hour

    # Reducing time in terms of 12 to find the period of AM or PM

    while  time_hour>=12:
        time_day = swapm(time_day)
        time_hour -= 12
        if time_day=='AM':  interval += 1
    # Formatiing mins (from 2 mins to 02 mins)
    if time_min//10==0:
        time_min = '0'+str(time_min)
    # Formatting time 
    if time_hour==0:    time_hour = 12
    # Generating sequence of time
    ans = str(time_hour)+':'+str(time_min)+' '+time_day
    # Calculating day (if given) using the found interval
    if not day is None :
        day = day.lower().capitalize()
        temp = interval % 7
        temp += days.index(day)
        temp %= 7
        day = days[temp]
        ans += ', '+day
    if interval == 1:
        ans+=' (next day)'
    elif interval > 1:
        ans+=' ('+str(interval)+' days later)'
    print (ans)
    return ans.rstrip()
    #return new_time