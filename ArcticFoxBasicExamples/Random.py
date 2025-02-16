
import random 



# Example 1
# Random can be used to create a random value or a list
# of random numbers. This example creates a random value
# between 0 and 1, which is Random's default behavior.
#
# Seed being used: #> Exists csvs/names.csv 
# ******************************************************
# ******************************************************

#> Random 
randomValue = random.random() 

#> print 
print(randomValue) #)1 
##*** 0.8064397621180912



# Example 2
# This example creates a random value between 50 and 100
# by specifying the bounds.
#
# Seed being used: #> Random --min 50 --max 100 
# ******************************************************
# ******************************************************

#> Random --min 50 --max 100 
randomValue_1 = random.uniform(50, 100) 

#> print 
print(randomValue_1) #)2 
##*** 79.36947171066589



# Example 3
# This example creates a random value between 50 and 100
# by specifying the bounds, BUT, this time, it specifies
# that the result should be an integer.
#
# Seed being used: #> Random --min 50 --max 100 --int 
# ******************************************************
# ******************************************************

#> Random --min 50 --max 100 --int 
randomValue_2 = random.randint(50, 100) 

#> print 
print(randomValue_2) #)3 
##*** 65



# Example 4
# Create a list of random numbers.
#
# Seed being used: #> Random --list 
# ******************************************************
# ******************************************************

#> Random --list 
randomList = [random.random() for __ in range(100)] 

#> print 
print(randomList) #)4 
##*** [0.30308563802524424, 0.4512553481312226, 0.9850995396388661, 0.9132692470307259, 0.012238043483916439, 0.39821886524394046, 0.3745013962888061, 0.9033604147248704, 0.94942475655903, 0.13065197738905465, 0.9138340155309195, 0.5271811575752824, 0.7769465722663447, 0.8586627977283883, 0.9033102141569892, 0.49905376081124175, 0.5878761050238511, 0.2547333586691197, 0.37289181396335214, 0.5328813111206173, 0.18298518257210528, 0.9051470502462446, 0.36854553759153497, 0.9274653810745472, 0.5589231189681328, 0.9403879800127494, 0.08540053330833575, 0.23212130074792836, 0.23266299674977697, 0.6620133527103328, 0.663600073638508, 0.6119797577691353, 0.1903120088668132, 0.7291100774001271, 0.3254313899180241, 0.9434621611145961, 0.06515627735517437, 0.6286401910213147, 0.549167534331334, 0.22912875695677526, 0.052129556591075654, 0.3147713400316908, 0.6109854584102455, 0.6065300492423059, 0.08604881598350822, 0.9813123272392641, 0.9696602151788452, 0.8265199357262584, 0.8227283471415489, 0.5444382878064391, 0.4911119620516451, 0.1261707586096329, 0.9702723104341101, 0.3708675564072408, 0.7793488278167966, 0.08837857331522248, 0.8678380490583285, 0.19825665963660388, 0.8370154004133051, 0.4344940531490392, 0.06839302831681482, 0.5032813410234609, 0.9002176375684654, 0.10738365195221433, 0.6275941875229466, 0.3856003812654887, 0.29121974801257977, 0.13778507335411805, 0.7135188620020841, 0.5111340117341657, 0.47311144690136475, 0.41358557101126703, 0.05946906826819143, 0.30283122566170717, 0.3035403965223281, 0.8547391320416703, 0.4096498007587617, 0.8801811870084203, 0.21294311043623204, 0.7763857694875302, 0.3920367442842718, 0.46891954968027605, 0.2529918144035864, 0.6512560925521242, 0.8643751769227256, 0.24817316368432785, 0.7164557093145979, 0.8580380088510521, 0.36195468889064775, 0.795872257181559, 0.5727333987782677, 0.6857556671481431, 0.16630054877383615, 0.3082671959953369, 0.23681715490896293, 0.04694956977677589, 0.2538052475033572, 0.003585181465400211, 0.10522440304248437, 0.42289828508039906]



# Example 5
# Create a list of random numbers and specify the size of
# the list.
#
# Seed being used: #> Random --list --count 10 
# ******************************************************
# ******************************************************

#> Random --list --count 10 
randomList_1 = [random.random() for __ in range(10)] 

#> print 
print(randomList_1) #)5 
##*** [0.8205845839623677, 0.5297569066375755, 0.08017196203555199, 0.5389564081815128, 0.30932283542775507, 0.40146411188580255, 0.42291684933638274, 0.49503597947121003, 0.3264245988311998, 0.38242210827644396]



# Example 6
# Create a list of random numbers, specify the size of
# the list, and specify that the are to be integers within
# a stated range.
#
# Seed being used: #> Random --list 
# ******************************************************
# ******************************************************

#> Random --list --count 20 --int --min -50 --max 50 
randomList_2 = [random.randint(-50, 50) for __ in range(20)] 

#> print 
print(randomList_2) #)6 
##*** [34, 22, -26, -17, -3, -38, -27, 9, -2, 4, 30, 42, -26, 3, -46, -38, 45, 33, 8, -37]

