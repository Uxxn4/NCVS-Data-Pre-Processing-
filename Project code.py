#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[264]:


# since the data is large, here I read only the first row to get columns names. 
incident_file = pd.read_csv("/Users/abdulrahmanalruways/Downloads/ICPSR_38430_3/DS0003/38430-0003-Data.tsv",sep="\t", nrows=1 )
# The data has 1017 variables.

# After reading the columns, I re-read the data using just the columns that I might need by apllying usecols parameter  
incident_file1 = pd.read_csv("/Users/abdulrahmanalruways/Downloads/ICPSR_38430_3/DS0003/38430-0003-Data.tsv",sep="\t",  usecols=['YEAR', 'IDHH','V3013','V3014','V3015','V3016','V3017','V3018','V3019','V3020','V3022','V3023','V3023A','V3024','V3024A','V3074','V3075','V3076','V3078','IDPER','V4014','V4015','V4020','V4021','V4021B','V4022','V4023','V4024','V4025','V4042','V4048','V4049','V4050','V4051','V4052','V4053','V4054','V4055','V4056','V4057','V4060','V4062','V4063','V4064','V4065','V4066','V4067','V4068','V4069','V4070','V4071','V4072','V4073','V4074','V4075','V4077','V4078','V4078','V4079','V4080','V4081','V4082','V4083','V4083','V4084','V4085','V4086','V4087','V4088','V4089','V4090','V4091','V4093','V4094','V4095','V4096','V4097','V4098','V4099','V4100','V4101','V4102','V4103','V4104','V4105','V4106','V4107','V4110','V4127','V4137','V4140A','V4210','V4211','V4234','V4236','V4237','V4243','V4245','V4247','V4249','V4250','V4251','V4252','V4286','V4210','V4399','V4422','V4437','V4478','V4467','V4481','V4481B','V4482','V4482A','V4482B','V4483','V4484','V4485','V4485A','V4486','V4528','V4529'])


# In[313]:


# before I start cleaning the data, I will reduce the size of the data by subsetting the data to have only workplace incidents.

# here the value 1 in V4484 variable indicates that incident happened at workplace 
incident_file1= incident_file1.loc[incident_file1['V4484']== 1 ] 
incident_file1



# In[267]:


# individual's education variable V3020 has some repeated entries for the same degree. 
# For Example, from 1 to 8 refer to (Elementary) , from 9 to 12 refer to (High school) , and from 21 to 26 refer to (College)

# To organize this column, I will create a new value and label as the following : 
#1= Elementary
#2= High School
#3= College
#4= Kindergarten
#5= 12th Grade 
#6= Diploma or equivalent 
#7 =Some college (but not finished)
#8 =Associate degree
#9 =Bachelor Degree
#10 =Master Degree 
#11 =Prof School Degree 
#12 =Doctorate degree



incident_file1['V3020'] = incident_file1['V3020'].replace([1, 2, 3,4,5,6,7,8],1)
incident_file1['V3020'] = incident_file1['V3020'].replace([9, 10, 11,12],2)
incident_file1['V3020'] = incident_file1['V3020'].replace([21, 22, 23,24,25,26],3)
incident_file1['V3020'] = incident_file1['V3020'].replace([0],'4')
incident_file1['V3020'] = incident_file1['V3020'].replace([27],'5')
incident_file1['V3020'] = incident_file1['V3020'].replace([28],'6')
incident_file1['V3020'] = incident_file1['V3020'].replace([40],'7')
incident_file1['V3020'] = incident_file1['V3020'].replace([41],'8')
incident_file1['V3020'] = incident_file1['V3020'].replace([42],'9')
incident_file1['V3020'] = incident_file1['V3020'].replace([43],'10')
incident_file1['V3020'] = incident_file1['V3020'].replace([44],'11')
incident_file1['V3020'] = incident_file1['V3020'].replace([45],'12')
incident_file1['V3020'] = incident_file1['V3020'].replace([99],'N/A') # this is the Residue value 
incident_file1['V3020'] = incident_file1['V3020'].replace([98],'N/A') # this is the out of universe value 







# In[271]:



# what time the incident occur(V4021,V4021B). 
# There are two variable for that,old and new. Because it was expanded from 7 answer categories to 9. 
# I will merge the two columns into one variable using the following value.

# these value were taken from both time variables (V4021,V4021B)
#1 = After 6 am. to 12 noon
#2 = After 12 noon to 3 pm.
#3 = After 3 pm. to 6 pm. 
#4 = After 12 noon to 6 pm.
#5 = After 6 pm. To 9 pm. 
#6 = After 9 pm. To 12 midnight.
#7 = After 6 pm. To 12 midnight
#8 = After 12 midnight To 6 am. 
#9 = Don't  Know what time of night 
#10= Don’t know what time of day 
#11= Don't know wether day or night 



def time_func(x):
    if (x['V4021'] == 1):
        return '1'
    elif (x['V4021B'] == 1):
        return '1'
    elif (x['V4021B'] == 2):
        return '2'
    elif (x['V4021B'] == 3):
        return '3'
    elif (x['V4021'] == 2):
        return '4'
    elif (x['V4021B'] == 5):
        return '5'
    elif (x['V4021B'] == 6):
        return '6'
    elif (x['V4021'] == 4):
        return '7'
    elif (x['V4021'] == 5):
        return '8'
    elif (x['V4021B'] == 7):
        return "8"
    elif (x['V4021'] == 6):
        return '9'
    elif (x['V4021B'] == 8):
        return "9"
    elif (x['V4021'] == 3):
        return '10'
    elif (x['V4021B'] == 4):
        return "10"
    elif (x['V4021'] == 7):
        return '11'
    elif (x['V4021B'] == 9):
        return "11"
    else:
        return 'N/A'
    
    
    
# create a new column for the time of incident based on our function 
incident_file1 = incident_file1.assign(Time_of_incident=incident_file1.apply(time_func, axis=1))



# In[283]:


# I'm going to create a new variable that shows if the incident happened during the day or the night. 
# I will re-categorize the time into 12 hours periods.
# Therefore, Daytime is from sunrise (this varies, but we can say approximately 6am) to sunset (we can say approximately 6pm). Night-time is from sunset to sunrise.
# The new variable will depend on the category of the column that I created before (Time_of_incident) 

#1 = After 6 am. to 12 noon = DayTime
#2 = After 12 noon to 3 pm.= DayTime
#3 = After 3 pm. to 6 pm. = DayTime
#4 = After 12 noon to 6 pm. = DayTime
#5 = After 6 pm. To 9 pm. = Nightime
#6 = After 9 pm. To 12 midnight.= Nightime
#7 = After 6 pm. To 12 midnight = Nightime
#8 = After 12 midnight To 6 am. = Nightime
#9 = Don't  Know what time of night = Nightime
#10= Don’t know what time of day = DayTime
#11= Don't know wether day or night = Don't know wether day or night 


# and it will take the following value : 1 = DayTime , 2= Nightime , 3= Don't know wether day or night 

def day_night_func(x):
    if (x['Time_of_incident'] == '1'):  
        return 1
    elif (x['Time_of_incident'] == '2'):
        return 1
    elif (x['Time_of_incident'] == '3'):
        return 1
    elif (x['Time_of_incident'] == '4'):
        return 1
    elif (x['Time_of_incident'] == '5'):
        return 2
    elif (x['Time_of_incident'] == '6'):
        return 2
    elif (x['Time_of_incident'] == '7'):
        return 2
    elif (x['Time_of_incident'] == '8'):
        return 2
    elif (x['Time_of_incident'] == '9'):
        return 2
    elif (x['Time_of_incident'] == '10'):
        return 1
    elif (x['Time_of_incident'] == '11'):
        return 3
    else:
        return 'N/A'


    
# create a new column called day_night based on our function.   
incident_file1 = incident_file1.assign(day_night=incident_file1.apply(day_night_func, axis=1))




# In[286]:


#'V4049' = DID OFFENDER HAVE A WEAPON, Take 1 as yes , 2 as No , 3 as don't know , 8 and 9 missing values 
#'V4050' = what was the weapon, take 1 if the one of the next seven variables have 1 , take 3 as Yes-Type Weapon-NA" , take 7 as "Gun Type Unknown", and 9 as missing value
#'V4051' = 'HAND GUN',
#'V4052' = 'other gun',
#'V4053' = 'knife',
#'V4054' = 'sharp object',
#'V4055' = 'Blunt object ',
#'V4056' = 'other weapon',
#'V4057' = 'Gun type unknown',


# create a function to merge the gun type variables into one column.
# that columns will be numerical with the description as shown below.
#1=Hand Gun
#2=Other Gun 
#3=Knife
#4=Sharp Object 
#5=Blunt Object
#6=Other Weapon
#7=Gun Type Unknown 
#8=No Weapon Used 
#9=Yes-Type Weapon-NA
#10=Don’t know if the offender have weapon

def weapon_type(x):
    if (x['V4051'] == 1):
        return '1'
    elif (x['V4052'] == 1):
        return '2'
    elif (x['V4053'] == 1):
        return '3'
    elif (x['V4054'] == 1):
        return '4'
    elif (x['V4055'] == 1):
        return '5'
    elif (x['V4056'] == 1):
        return '6'
    elif (x['V4057'] == 1):
        return '7'
    elif (x['V4049'] == 2):
        return '8'
    elif (x['V4050'] == 3):
        return '9'
    elif (x['V4049'] == 3):
        return "10"
    else:
        return 'N/A'


# create a new column called Type_of_weapon based on our function.   
incident_file1 = incident_file1.assign(Type_of_weapon=incident_file1.apply(weapon_type, axis=1))







# In[ ]:





# In[303]:


#'V4065' =  what happened
#'V4066' =  something_taken <- take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe
#'V4067' =  ATTEMPTED_THEFT  <- take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe
#'V4068' =  Harassed_abusive_language  <- take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe
#'V4069' =  sexual_contact_with_force  <- take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe
#'V4070' =  sexual_contact_without_force <- take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe
#'V4071' =  forcible entry of house/apartment <- take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe
#'V4072' =  forcible_entry_of_car <- take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe
#'V4073' =  PROPERTY_DAMAGE <-  take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe
#'V4074' =  Attempted_PROPERTY_DAMAGE  <- take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe
#'V4075' =  OTHER_TYPE_INCIDENT  <- take 0 as no , 1 as yes , 8 as Residue, and 9 as Out of universe



# The above columns provide information about the incident.
# I  will merge those columns into one columns named [what_happened] and that column will take the following value :- 

# 1 = something taken
# 2 = ATTEMPTED_THEFT
# 3 = Harassed, argument, abusive language
# 4 = sexual contact with force
# 5 = sexual contact without force
# 6 = forcible entry of house/apartment 
# 7 = forcible entry of car
# 8 = PROPERTY DAMAGE
# 9 = Attempted PROPERTY DAMAGE
# 10 = OTHER TYPE INCIDENT
def what_happen(x):
    if (x['V4066'] == 1):
        return '1'
    elif (x['V4067'] == 1):
        return '2'
    elif (x['V4068'] == 1):
        return '3'
    elif (x['V4069'] == 1):
        return '4'
    elif (x['V4070'] == 1):
        return '5'
    elif (x['V4071'] == 1):
        return '6'
    elif (x['V4072'] == 1):
        return '7'
    elif (x['V4073'] == 1):
        return '8'
    elif (x['V4074'] == 1):
        return '9'
    elif (x['V4075'] == 1):
        return '10'
    else:
        return 'N/A'
    
    

    

# create a new column called What_happened based on our function.   
incident_file1 = incident_file1.assign(What_happened=incident_file1.apply(what_happen, axis=1))

    


# In[307]:


# The following two columns ask the victim if the offender try to attack or threaten the victim 
# 'V4062' = Did the offender TRY to attack you? 
# 'V4064' = Did the offender THREATEN you with harm in any way

# If one of the previous variables have the value of 1 (Yes), The next 14 variables are describing how the offender did that.

# V4077 - LI HOW OFF THREATENED OR TRIED TO ATTACK 

# V4078 Verbal threat of rape    <- will take the value of 1 in the new variable (V4077A)
# V4079 Verbal threat to kill = <- will take the value of 2 in the new variable (V4077A)
# V4080 Verbal threat of attack other than to kill or rape <- will take the value of 3 in the new variable (V4077A)
# V4081 Verbal threat of sexual assault other than rape <- will take the value of 4 in the new variable (V4077A)
# V4082 Unwanted sexual contact with force (grabbing, fondling, etc.) <- will take the value of 5 in the new variable (V4077A)
# V4083 Unwanted sexual contact without force (grabbing, fondling, etc.)<- will take the value of 6 in the new variable (V4077A)
# V4084 Weapon present or threatened with weapon <- will take the value of 7 in the new variable (V4077A)
# V4085 Shot at (but missed) <- will take the value of 8 in the new variable (V4077A)
# V4086 Attempted attack with knife/sharp weapon  <- will take the value of 9 in the new variable (V4077A)
# V4087 Attempted attack with weapon other than gun/knife/sharp weapon  <- will take the value of 10 in the new variable (V4077A)
# V4088 Object thrown at person  <- will take the value of 11 in the new variable (V4077A)
# V4089 Followed or surrounded  <- will take the value of 12 in the new variable (V4077A)
# V4090 Tried to hit, slap, knock down, grab, hold, trip, jump, push, etc. <- will take the value of 13 in the new variable (V4077A)


# I going to create a function to merge those variables into one variable called V4077A 

def how_threat_tryAttack(x):
    if (x['V4078'] == 1):
        return '1'
    elif (x['V4079'] == 1):
        return '2'
    elif (x['V4080'] == 1):
        return '3'
    elif (x['V4081'] == 1):
        return '4'
    elif (x['V4082'] == 1):
        return '5'
    elif (x['V4083'] == 1):
        return '6'
    elif (x['V4084'] == 1):
        return '7'
    elif (x['V4085'] == 1):
        return '8'
    elif (x['V4086'] == 1):
        return '9'
    elif (x['V4087'] == 1):
        return '10'
    elif (x['V4088'] == 1):
        return '11'
    elif (x['V4089'] == 1):
        return '12'
    elif (x['V4090'] == 1):
        return '13'
    else:
        return 'N/A'
    
    

    

# create a new column named V4077A based on our function.   
incident_file1 = incident_file1.assign(V4077A=incident_file1.apply(how_threat_tryAttack, axis=1))





# In[309]:


# The variable'V4093' ask the victim how  were you attacked ? If the value of this column is 1, 
# then the following variables are giving more detalis about how the victim was attacked. 
# I'm going to create a function in order to combined all the follwing variable into a single column named (V4093A)


#'V4094' = 'RAPED',                         <- will take the value of 1 in the new variable (V4093A)
#'V4095' = 'TRIED_TO_RAPE',                 <- will take the value of 2 in the new variable (V4093A)
#'V4096' = ' SEXUAL_ASSAULT',               <- will take the value of 3 in the new variable (V4093A)
#'V4097' = 'SHOT',                          <- will take the value of 4 in the new variable (V4093A)
#'V4098' = 'SHOT_but_MISSED',               <- will take the value of 5 in the new variable (V4093A)
#'V4099' = 'HIT_WITH_GUN',                  <- will take the value of 6 in the new variable (V4093A)
#'V4100' = 'STABBED',                       <- will take the value of 7 in the new variable (V4093A)
#'V4101' = 'Attempted_attack_with_knife',   <- will take the value of 8 in the new variable (V4093A) 
#'V4102' = 'Hit_by_object',                 <- will take the value of 9 in the new variable (V4093A)
#'V4103' = 'Hit_by_thrown_object',          <- will take the value of 10 in the new variable (V4093A)
#'V4104' = 'Attempted_attack_with_different_weapon',   <- will take the value of 11 in the new variable (V4093A)
#'V4105' = 'Hit_slapped_knocked_down',      <- will take the value of 12 in the new variable (V4093A)
#'V4106' = 'Grabbed_held_tripped_jumped_pushed',  <- will take the value of 13 in the new variable (V4093A)
#'V4107' = 'Other_type_of_attack',           <- will take the value of 14 in the new variable (V4093A)





def how_Attack(x):
    if (x['V4094'] == 1):
        return '1'
    elif (x['V4095'] == 1):
        return '2'
    elif (x['V4096'] == 1):
        return '3'
    elif (x['V4097'] == 1):
        return '4'
    elif (x['V4098'] == 1):
        return '5'
    elif (x['V4099'] == 1):
        return '6'
    elif (x['V4100'] == 1):
        return '7'
    elif (x['V4101'] == 1):
        return '8'
    elif (x['V4102'] == 1):
        return '9'
    elif (x['V4103'] == 1):
        return '10'
    elif (x['V4104'] == 1):
        return '11'
    elif (x['V4105'] == 1):
        return '12'
    elif (x['V4106'] == 1):
        return '13'
    elif (x['V4107'] == 1):
        return '14'
    else:
        return 'N/A'
    
    

    

# create a new column named V4093A based on our function.   
incident_file1 = incident_file1.assign(V4093A=incident_file1.apply(how_Attack, axis=1))





# In[323]:


# drop unnecessary columns 
incident_file1.drop(['V3013','V3016','V3017','V3022','V3024A'], axis =1)



# load the final data as csv 
incident_file1.to_csv("/Users/abdulrahmanalruways/Downloads\incident_file1.csv")


# In[ ]:




