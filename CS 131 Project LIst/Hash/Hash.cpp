// Hash.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "UnorderedMap.h"
#include "Movie.h"

using namespace std;

int main()
{
	UnorderedMap<Movie, int, Movie::Hashor, Movie::Equalitor> tCopiesTracker;

	tCopiesTracker.SetWithKey(Movie("Circle", 2015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Spider-Man: Far from Home", 2019, 120), 3);
	tCopiesTracker.SetWithKey(Movie("Omg did I say 50?", 2015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("What was I thinking?", 2013, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Actually, I was", 20155, 87), 4);
	tCopiesTracker.SetWithKey(Movie("thinking I'd just", 2015, 827), 4);
	tCopiesTracker.SetWithKey(Movie("make y'all do it.", 2011, 87), 4);
	tCopiesTracker.SetWithKey(Movie("But then", 2015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("I realized", 205515, 837), 4);
	tCopiesTracker.SetWithKey(Movie("the output had to be consistant", 2015, 87), 4);

	tCopiesTracker.SetWithKey(Movie("I pirouette in the dark", 223015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("I see the stars through a mirror", 2015, 82347), 4);
	tCopiesTracker.SetWithKey(Movie("Tired mechanical heart", 2015, 8447), 4);
	tCopiesTracker.SetWithKey(Movie("Beats 'til the song disappears", 23015, 8237), 4);
	tCopiesTracker.SetWithKey(Movie("Somebody shine a light", 245014, 87), 4);
	tCopiesTracker.SetWithKey(Movie("I'm frozen by the fear in me", 2015, 84567), 4);
	tCopiesTracker.SetWithKey(Movie("Somebody make me feel alive", 2015, 857), 4);
	tCopiesTracker.SetWithKey(Movie("And shatter me", 2015, 4487), 4);
	// Shatter Me; Lindsey Stirling (feat. Lzzy Hale)

	tCopiesTracker.SetWithKey(Movie("I, man, am regal - a German am I", 45015, 4587), 4);
	tCopiesTracker.SetWithKey(Movie("Never odd or even", 204515, 857), 4);
	tCopiesTracker.SetWithKey(Movie("If I had a hi-fi", 2115, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Madam, I'm Adam", 20215, 37), 4);
	tCopiesTracker.SetWithKey(Movie("Too hot to hoot", 2015, 827), 4);
	tCopiesTracker.SetWithKey(Movie("No lemons, no melon", 22015, 57), 4);
	tCopiesTracker.SetWithKey(Movie("Too bad I hid a boot", 2015, 827), 4);
	tCopiesTracker.SetWithKey(Movie("Lisa Bonet ate no basil", 2015, 827), 4);
	tCopiesTracker.SetWithKey(Movie("Warsaw was raw", 2015, 827), 4);
	tCopiesTracker.SetWithKey(Movie("Was it a car or a cat I saw?", 2015, 287), 4);
	// Bob; Weird Al Yankovic

	tCopiesTracker.SetWithKey(Movie("Heya Tom, it's Bob from the office down the hall", 20215, 87), 4);
	tCopiesTracker.SetWithKey(Movie("It's good to see you buddy, how've you been?", 20215, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Things have been OK for me except that I'm a zombie now", 20215, 87), 4);
	tCopiesTracker.SetWithKey(Movie("I really wish you'd let us in", 20315, 847), 4);
	tCopiesTracker.SetWithKey(Movie("I think I speak for all of us when I say I understand", 20155, 876), 4);
	tCopiesTracker.SetWithKey(Movie("Why you folks might hesitate to submit to our demand", 62015, 5), 4);
	tCopiesTracker.SetWithKey(Movie("But here's an FYI: you're all gonna die screaming", 20715, 87), 4);
	tCopiesTracker.SetWithKey(Movie("All we want to do is eat your brains", 26015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("We're not unreasonable, I mean, no one's gonna eat your eyes", 20155, 87), 4);
	tCopiesTracker.SetWithKey(Movie("All we want to do is eat your brains", 2015, 8557), 4);
	tCopiesTracker.SetWithKey(Movie("We're at an impasse here, maybe we should compromise:", 20145, 33), 4);
	tCopiesTracker.SetWithKey(Movie("If you open up the doors", 2015, 454587), 4);
	tCopiesTracker.SetWithKey(Movie("We'll all come inside and eat your brains", 20115, 8457), 4);
	// RE: Your Brains; Jonathan Coulton

	tCopiesTracker.SetWithKey(Movie("Have you ever felt that somehow", 20115, 87), 4);
	tCopiesTracker.SetWithKey(Movie("You were not yourself", 20115, 871), 4);
	tCopiesTracker.SetWithKey(Movie("That your body was the same", 1, 87), 4);
	tCopiesTracker.SetWithKey(Movie("But everything around you wasn't right", 1015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("And images so strange and foreign", 222015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Flooded in like raging water", 201335, 87), 4);
	// Good for Your Soul; Oingo Boingo

	tCopiesTracker.SetWithKey(Movie("Betamax: Circle", 2015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Spider-Man: Far from Home", 20519, 120), 3);
	tCopiesTracker.SetWithKey(Movie("Betamax: Omg did I say 50?", 2015, 857), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: What was I thinking?", 2013, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Actually, I was", 2015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: thinking I'd just", 20185, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: make y'all do it.", 2011, 8567), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: But then", 2015, 837), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: I realized", 2015, 867), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: the output had to be consistant", 202315, 87), 4);

	tCopiesTracker.SetWithKey(Movie("Betamax: I pirouette in the dark", 24015, 847), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: I see the stars through a mirror", 4, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Tired mechanical heart", 6, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Beats 'til the song disappears", 7, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Somebody shine a light", 3, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: I'm frozen by the fear in me", 256015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Somebody make me feel alive", 2015, 4), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: And shatter me", 2015, 4), 4);
	// Shatter Me; Lindsey Stirling (feat. Lzzy Hale)

	tCopiesTracker.SetWithKey(Movie("Betamax: I, man, am regal - a German am I", 2015, 3), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Never odd or even", 2015, 6), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: If I had a hi-fi", 52115, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Madam, I'm Adam", 20135, 37), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Too hot to hoot", 20715, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: No lemons, no melon", 2015, 57), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Too bad I hid a boot", 20515, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Lisa Bonet ate no basil", 2015, 877), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Warsaw was raw", 2015, 837), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Was it a car or a cat I saw?", 2015, 587), 4);
	// Bob; Weird Al Yankovic

	tCopiesTracker.SetWithKey(Movie("Betamax: Heya Tom, it's Bob from the office down the hall", 2015, 6), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: It's good to see you buddy, how've you been?", 777, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Things have been OK for me except that I'm a zombie now", 2, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: I really wish you'd let us in", 2015, 34587), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: I think I speak for all of us when I say I understand", 2034515, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Why you folks might hesitate to submit to our demand", 2345015, 5), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: But here's an FYI: you're all gonna die screaming", 2034515, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: All we want to do is eat your brains", 201455, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: We're not unreasonable, I mean, no one's gonna eat your eyes", 256015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: All we want to do is eat your brains", 2567015, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: We're at an impasse here, maybe we should compromise:", 203315, 33), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: If you open up the doors", 20415, 87), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: We'll all come inside and eat your brains", 201235, 87), 4);
	// RE: Your Brains; Jonathan Coulton

	tCopiesTracker.SetWithKey(Movie("Betamax: Have you ever felt that somehow", 2015, 43487), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: You were not yourself", 2015, 837), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: That your body was the same", 2015, 847), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: But everything around you wasn't right", 2015, 8733), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: And images so strange and foreign", 2015, 8447), 4);
	tCopiesTracker.SetWithKey(Movie("Betamax: Flooded in like raging water", 2015, 44487), 4);
	// Good for Your Soul; Oingo Boingo

	cout << tCopiesTracker.DebugDump();

	return 0;
}

