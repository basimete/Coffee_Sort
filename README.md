The Mission: What can I learn from categorising 150 latte art pours over 12 months?

The How: VSCode, Python, Vibecoding, Google Sheets. 

The Tools: Pandas, Matplotlib.

The live data : https://docs.google.com/spreadsheets/d/1EcOkLbCAZj2cvps9ZjwjKadoxVnKuSxfeSSETcY59so/edit?usp=sharing

The pretty version : https://www.canva.com/design/DAHCWD0akYA/fl5659Rjy6Z6aGocz5FGYw/edit?utm_content=DAHCWD0akYA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


What is this?
This project is a 17-month deep dive into my morning coffee habit. I tracked 140 flat whites to see if I was actually getting any better at latte art, or if I was just caffeinating myself in circles. It turns out, if you track enough pours, a story starts to emerge about how we learn new skills.

What I did (The Process)
Built a Coffee Log: I created a spreadsheet to track every drink. I didn't just look at the date; I rated the Texture (how silky the milk was), the Shape (how close it looked to a heart or a tulip), and even the Vibe of the morning.

Cleaned the "Messy" Parts: Sometimes I messed up the input or wrote the wrong thing. Whilst the code does have some protection from this type of human error - it's not foolproof. I used Python to tidy up those errors so the final charts wouldn't have any weird gaps.

Found the Learning Curves: I used code to draw a "line of best fit" through my scores. This helped me see past a single bad cup to see the bigger picture: Am I actually improving over the long run?

Measured the Good Stuff: I calculated the "Oat Milk Offset." By choosing plant-based milk for these 140 drinks, I worked out exactly how much water and CO2 I saved compared to using dairy.


What the Code  Does
If you run the script, it performs three jobs

1. The "Monthly Snapshot" Instead of looking at 140 individual dots (which is messy), the code groups the coffees by month. It calculates your average for each month so you can see the steady climb from Oct '24 to today.

2. The Comparison Test The code compares Texture vs. Shape. It proved that your milk steaming (Texture) improved much faster than your actual drawing (Shape). It turns out, mastering the steam wand is easier than mastering the pour!

3. The Eco-Counter The code acts like a calculator. It takes the total number of coffees (140) and multiplies them by environmental "savings" factors. It's a quick way to turn a sustainability report.

4. The Design Engine Finally, the code isn't just crunching numbers; it’s a tiny artist. It’s set up to skip the boring "default" look of Excel charts and instead create clean, minimalist graphs that look like they belong in a coffee zine or a professional presentation.
