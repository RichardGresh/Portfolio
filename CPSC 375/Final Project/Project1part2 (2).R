#Project 1 CPSC375
#Richard Gresham

library(ggplot2)
library(tidyverse)
library(class)
library(modelr)

# starting 1a).

bed <- read_csv("Hospitalbed.csv")
demo <- read_csv("Demographics.csv")
vactime <- read_csv("https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/global_data/time_series_covid19_vaccine_doses_admin_global.csv")

# starting 1b and 1g
# b). remove uneeded rows ...
vactime <- vactime %>% filter(Population >= 0, is.na(Province_State))

vactime <- vactime %>% select(-Admin2, -FIPS, -Province_State, -UID, -iso2, -iso3, -code3, -Lat, -Long_, -Combined_Key)

demo <- demo %>% select(-'Series Name', -`Country Code`)

# c). tidy data as needed.

vactime <- vactime %>% pivot_longer(c( -Country_Region, -Population), names_to = "date", values_to = "shots", values_drop_na = TRUE)
vactime <- vactime %>% filter(shots > 0)



demo <- demo %>% pivot_wider(names_from = "Series Code", values_from = YR2015)


# d). calculate vaccination rate which is shots / population

vactime <- vactime %>% mutate(vacrate = shots/Population)



# e). number of days since vaccination began, calculate a variable that is: number of days since first non-zero vaccination number. This variable will be important for modeling.

vactime <- vactime %>% group_by (Country_Region) %>% mutate(days_since_start = 1:n())

# f). Discard data that is not needed.

vactime <- vactime %>% select(-date) #don't need date anymore.

 #this gives us a bed data frame with only the most recent year
bed <- bed %>% rename(beds = `Hospital beds (per 10 000 population)`)
bed <- bed %>% group_by(Country) %>% filter(Year == max(Year)) %>% select(Country, beds) #gives us hospital bed number from most recent year



#g). now we work on demographics 
demo_merged <- demo %>% mutate(SP.POP.80UP=SP.POP.80UP.FE+SP.POP.80UP.MA) %>% mutate(SP.POP.1564.IN=SP.POP.1564.MA.IN+SP.POP.1564.FE.IN) %>% mutate(SP.POP.0014.IN=SP.POP.0014.MA.IN+SP.POP.0014.FE.IN) %>% mutate(SP.DYN.AMRT=SP.DYN.AMRT.MA+SP.DYN.AMRT.FE) %>% mutate(SP.POP.TOTL.IN=SP.POP.TOTL.FE.IN+SP.POP.TOTL.MA.IN) %>% mutate(SP.POP.65UP.IN=SP.POP.65UP.FE.IN+SP.POP.65UP.MA.IN) %>% select(-contains(".FE")) %>% select(-contains(".MA"))


demo <- demo_merged %>% group_by(`Country Name`) %>%   summarise(SP.DYN.LE00.IN = sum(SP.DYN.LE00.IN, na.rm = TRUE),
                                                                 SP.URB.TOTL= sum(SP.URB.TOTL, na.rm = TRUE),
                                                                 SP.POP.TOTL= sum(SP.POP.TOTL, na.rm = TRUE),
                                                                 SP.POP.80UP= sum(SP.POP.80UP, na.rm = TRUE),
                                                                 SP.POP.1564.IN= sum(SP.POP.1564.IN, na.rm = TRUE),
                                                                 SP.POP.0014.IN= sum(SP.POP.0014.IN, na.rm = TRUE),
                                                                 SP.DYN.AMRT= sum(SP.DYN.AMRT, na.rm = TRUE),
                                                                 SP.POP.TOTL.IN= sum(SP.POP.TOTL.IN, na.rm = TRUE),
                                                                 SP.POP.65UP.IN= sum(SP.POP.65UP.IN, na.rm = TRUE))

demo <- demo %>% select(`Country Name`, SP.URB.TOTL, SP.DYN.LE00.IN)
# h). 

#combining country names
#Iran
demo <- demo %>% mutate(`Country Name` = replace(`Country Name`, `Country Name` == "Iran, Islamic Rep.", "Iran"))
bed <- bed %>% mutate(Country = replace(Country, Country == "Iran (Islamic Republic of)", "Iran"))
#South Korea
demo <- demo %>% mutate(`Country Name` = replace(`Country Name`, `Country Name` == "Korea, Rep.", "South Korea"))
bed <- bed %>% mutate(Country = replace(Country, Country == "Republic of Korea", "South Korea"))
vactime <- vactime %>% mutate(Country_Region = replace(Country_Region, Country_Region == "Korea, South", "South Korea"))
#United Kingdom
bed <- bed %>% mutate(Country = replace(Country, Country == "United Kingdom of Great Britain and Northern Ireland", "United Kingdom"))
#only one in the three data sets there needed to be changed.
#now onto merging the three data frames.

covid <- vactime %>% inner_join(bed, by = c(Country_Region = "Country")) %>% inner_join(demo, by = c(Country_Region = "Country Name"))
view(covid)
covid <- covid %>% rename(Country = Country_Region)
covid <- covid[,c(1,4,3,2,5,6,8,7)]

covid_latestday <- covid %>% arrange(-days_since_start) %>% group_by(Country) %>% slice(1)
ggplot(data = covid_latestday) + geom_point(mapping = aes(x = days_since_start, y = vacrate))

#here we will have 5 linear regression models, and we will be using the best one.
m1 <- lm(data = covid, formula = vacrate ~ days_since_start)
summary(m1)
#returns R2 of .5372(adjusted .5371)
m2 <- lm(data = covid, formula = vacrate ~ SP.URB.TOTL/beds)
summary(m2)
#returns R2 of .01324(adjusted .01321)
m3 <- lm(data = covid, formula = vacrate ~ days_since_start + SP.URB.TOTL)
summary(m3)
#returns R2 of .5394(adjusted .5394)
m4 <- lm(data = covid, formula = vacrate ~ SP.URB.TOTL)
summary(m4)
#returns R2 of .003049(adjusted .003035)
m5 <- lm(data = covid, formula = vacrate ~ days_since_start + SP.DYN.LE00.IN)
summary(m5)
# returns R2 of .7078(adjusted .7078) This is the highest of the 5 and the one I will choose.

#summary bar graph with the R2 values on the y axis and the corresponding model name on the x-axis.
lrmodel <- data.frame(Model = c("m1", "m2", "m3", "m4", "m5"), R2 = c(.5371, .01321, .5394, .003035, .7078))
ggplot(data = lrmodel, aes(x = Model, y = R2)) + geom_bar(stat = "identity")
