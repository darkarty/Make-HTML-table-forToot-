from input import peopleObjects;

# Open/write to output.html
output = open("output.html","w")

# Assign list of dicts to people
people = peopleObjects();

# Sort according to last name
peopleSorted = sorted(people, key=lambda k: k['lastname'])

# Write html table
output.write('<table style="height: 498px;border-color: #ffffff;width: 1037px" border="0" cellspacing="10" cellpadding="15">\n')
output.write('<tbody>\n')

count = 0

for person in peopleSorted:

	# Write at the beginning of every 2 entries (two columns per row)
	if(count%2 == 0):
		output.write('<tr style="height: 193px">\n')

	output.write('<td style="background-color: #ffffff;border-color: #ffffff;width: 499px;height: 193px">\n')
	output.write('<h3 style="padding-left: 60px;text-align: center">\n')
	output.write('<span style="color: #000000">\n')
	output.write('<a href="' + person['link'] + '">\n')
	output.write('<img class="alignleft wp-image-735 size-full" src="' + person['profileHref'] + '" alt="" width="156" height="156">' + person['lastname'] + ', ' 
		+ person['firstname'] + '</a>\n')
	output.write('</span>\n</h3>\n')
	output.write('<h5 style="padding-left: 30px;text-align: center"><span style="color: #000000"> '+"PERSON'S AREA" + '</span></h5>\n')
	output.write('</td>\n')

	count = count + 1;

	# Write if at the end of every two entries (two columns per row)
	if(count == 2):
		output.write('</tr>\n')
		count = 0

# If the last row only has one column, then end the row
if(count == 1):
	output.write('</tr>\n')

# Original seems to have some blank entries at the bottom
output.write('<tr style="height: 24px">\n')
output.write('<td style="background-color: #ffffff;border-color: #ffffff;width: 499px;height: 24px"></td>\n')
output.write('<td style="background-color: #ffffff;border-color: #ffffff;width: 446px;height: 24px"></td>\n')
output.write('</tr>')

# Close table tags
output.write('</tbody>\n')
output.write('</table>')

# CLose file
output.close()