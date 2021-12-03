import sys




def groupschedule (pers1Schedule, pers1DailyAct, pers2Schedule, pers2DailyAct,duration ):

    updatedSchedule1 = updateSchedule(pers1Schedule, pers1DailyAct)
    updatedSchedule2 = updateSchedule(pers2Schedule, pers2DailyAct)
    mergedSchedule= mergedSchedules(updatedSchedule1, updatedSchedule2)
    CombineSchedules= sortedAllSchedules(mergedSchedule)
    print (matchedAvailabilities(CombineSchedules,duration))


def updateSchedule(Schedule, DailyAct):
    copyschedule = list()
    temp = ''
    templist = list()
    in_brackets = False
    for x in range(1, len(Schedule) - 1):
        itsabracket = False
        itsacomma = False
        itsnotallowed = False

        if Schedule[x] == '’' or Schedule[x] == '‘' or Schedule[x] == ' ' or Schedule[x] == "'" :

            itsnotallowed = True
        if Schedule[x] == '[':
            in_brackets = True
            itsabracket = True
        if in_brackets == True and (Schedule[x] == ',' or Schedule[x] == ']'):
            itsacomma = True
            templist.append(temp)
            temp =''
        if Schedule[x] == ']':
            in_brackets = False
            itsabracket = True
            copyschedule.append(templist)
            templist = list()
        
        
        if in_brackets == True and itsacomma == False and itsabracket == False and itsnotallowed == False:
            temp = temp + Schedule[x]

    DailyFreeTime = list()
    temp =''
    in_brackets = False
    
    for y in range(0, len(DailyAct)):
        itsabracket = False
        itsacomma = False
        itsnotallowed = False

        if DailyAct[y] == '’' or DailyAct[y] == '‘' or DailyAct[y] == ' ' or DailyAct[y] == "'" :

            itsnotallowed = True
        if DailyAct[y] == '[':
            in_brackets = True
            itsabracket = True
        if in_brackets == True and (DailyAct[y] == ',' or DailyAct[y] == ']'):
            itsacomma = True
            DailyFreeTime.append(temp)
            temp =''
        if DailyAct[y] == ']':
            in_brackets = False
            itsabracket = True
            
   
        if in_brackets == True and itsacomma == False and itsabracket == False and itsnotallowed == False:
            temp = temp + DailyAct[y]

    copyschedule.insert(0, ['0:00', DailyFreeTime[0]])  #update unavailable schedules and add early morning hours
    copyschedule.append([DailyFreeTime[1], '23:59'])   #update unavailable schedules and add after work hours
  
   
    
    return copyschedule
    #return list(map(lambda s: [convertToMinutes(s[0]), convertToMinutes(s[1])], updatedSchedule))


def mergedSchedules(pers1Schedule, pers2Schedule): #this function merges time schedules in order of the earliest time in the 1st position in nested loops 
    merged =list()

    i,j = 0,0
    while i < len(pers1Schedule) and j< len(pers2Schedule):
        meeting1, meeting2 = pers1Schedule[i],pers2Schedule[j] #saying set meeting 1 equal to i list in list pers1, and same for meeting2
        if convertToMinutes(meeting1[0]) == convertToMinutes(meeting2[0]):
            if convertToMinutes(meeting1[1]) < convertToMinutes(meeting2[1]):
                merged.append(meeting1)
                i+=1
            if convertToMinutes(meeting1[1]) > convertToMinutes(meeting2[1]):
                merged.append(meeting2)
                j+=1
            if convertToMinutes(meeting1[1]) == convertToMinutes(meeting2[1]):
                merged.append(meeting1)
                j+=1
                i+=1
        if convertToMinutes(meeting1[0]) < convertToMinutes(meeting2[0]):
            merged.append(meeting1)
            i+=1
        if convertToMinutes(meeting1[0]) > convertToMinutes(meeting2[0]):
            merged.append(meeting2)
            j+=1

    while i < len(pers1Schedule):
        merged.append(meeting1)
        i+=1
    while j < len(pers2Schedule):
        merged.append(meeting2)
        j+=1
   
    
    return merged

   
def sortedAllSchedules (Schedule, start_index = 0): #this function will read through our nested list and combine times that appear in same time frame. 
    merged = [False for i in range(0,len(Schedule))]
    result = list()
    for i in range(0, len(Schedule)):
        for j in range(i + 1 , len(Schedule) - 1):
            merged[i] = merged[i] or merge(Schedule[i],Schedule[j])
        if(i + 1 == len(Schedule)):
            merged[i] = True
    for i in range(0, len(Schedule)):
        if (merged[i] == False):
            result.append(Schedule[i])
               




 
    return result

  
    #Todo: write a function to  arrange all schedules. New meeting starts AFTER the end of current meeting.
def merge(meeting1, meeting2):
    if convertToMinutes(meeting1[1]) < convertToMinutes(meeting2[0]) or meeting2[1] < meeting1[0]:
        return False

    placeholder1 = min(convertToMinutes(meeting1[0]), convertToMinutes(meeting2[0]))
    placeholder2 = max(convertToMinutes(meeting1[1]), convertToMinutes(meeting2[1]))
    meeting2[0] = convertMinutestoHour(placeholder1)
    meeting2[1] = convertMinutestoHour(placeholder2)

    return True
    

def matchedAvailabilities(Schedule, duration):
    availabilities= list()
    availabletimes = list()
    j = 0
    for i in range(0, len(Schedule) - 1):
        temp = list()
        temp.append(Schedule[i][1])
        temp.append(Schedule[i+1][0])
        availabilities.append(temp)


    for j in range(0, len(availabilities)):
        temp = list()
        breaktime = convertToMinutes(availabilities[j][1]) - convertToMinutes(availabilities[j][0])
        if(breaktime >= int(duration)):
            temp.append(availabilities[j][0])
            temp.append(availabilities[j][1])
            availabletimes.append(temp)


        

    return availabletimes
    
   #Todo: write a function to match all availabilities
    


def convertToMinutes(time):
  
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes

def convertMinutestoHour(minutes):
    hours = minutes // 60
    mins = minutes% 60
    toString = str(hours)
    toStringMins = "0" + str(mins) if mins< 10 else str(mins)
    return toString +":" + toStringMins

def main():
    pers1Schedule = input("Enter schedule for person 1:")
    pers2Schedule = input("Enter schedule for person 2:")
    pers1DailyAct = input("Enter Daily Availability for pers 1: ")
    pers2DailyAct = input("Enter Daily Availability for pers 2: ")
    duration = input("Enter duration of the proposed meeting: ")
    groupSchedule1= groupschedule (pers1Schedule, pers1DailyAct, pers2Schedule, pers2DailyAct,duration )

if __name__ == "__main__":
    main()
