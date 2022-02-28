import re
def format_duration(seconds):
    secs = 0
    minutes = 0
    hours = 0
    days = 0
    years = 0
    duration_list_s = []
    duration_list = []
    if seconds == 0:
        return 'now'
    while seconds > 0:                                                                      # It will keep looping if seconds is higher than 0
        if seconds >= 31536000:                                                             # a year has 31556926 seconds
            seconds -= 31536000
            years += 1 
        elif seconds >= 86400 and not seconds >= 31536000:                                  # if the amount of seconds is more than a year, 
            seconds -= 86400                                                                # it should do year += 1 first before going to this section
            days += 1                                                                       # 1d = 86400 seconds
        elif seconds >= 3600 and not seconds >= 86400:                                      # same concept as above, 3600 seconds = 1 hour
            seconds -= 3600
            hours += 1
        elif seconds >= 60 and not seconds >= 3600:
            seconds -= 60
            minutes += 1
        elif seconds >= 1 and not seconds >= 60:
            seconds -= 1
            secs += 1
    
    duration_wrong_format = f'{years} years {days} days {hours} hours {minutes} minutes {secs} seconds'  # example: '1 year 50 days 0 hours 0 minutes 1 seconds'
    pattern = re.compile('\d+\s\w+')                                                        # pattern(digit > white space > word) = '1 year', '50 days' '0 days' etc
    duration_list_zero = pattern.findall(duration_wrong_format)                                          # List for the pattern. 
    for time in duration_list_zero:                                                         # Problem is that it still has 0 days and 0 hours which we need to remove. 
        if time.startswith('0'):                                                             #if the string starts with a 0 do nothing
            pass
        else:                                                                               # if the string doesn't start with a 0 then it needs to add this string to the list
            duration_list_s.append(time)
    for time in duration_list_s:                                                            # the reason it's called duration_called_s is because 
        if re.match('1\s', time):                                                             # the string always ends with s even though its just one number (1 seconds)
            duration_list.append(time[:-1])                                                 # the [:-1] excludes the last letter, so if it start with zero, for example 
        else:                                                                               # 0 seconds, it will become 0 second.
            duration_list.append(time)                                                  
    if len(duration_list) == 1:                                                             # depending on how many times are in the list we need to add 'and' and ','
            return(duration_list[0])
    elif len(duration_list) == 2:
        return(f'{duration_list[0]} and {duration_list[1]}')
    elif len(duration_list) == 3:
        return(f'{duration_list[0]}, {duration_list[1]} and {duration_list[2]}')
    elif len(duration_list) == 4:
        return(f'{duration_list[0]}, {duration_list[1]}, {duration_list[2]} and {duration_list[3]}')
    elif len(duration_list) == 5:
        return(f'{duration_list[0]}, {duration_list[1]}, {duration_list[2]}, {duration_list[3]} and {duration_list[4]}')