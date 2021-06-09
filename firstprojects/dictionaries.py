monthConversions = {
        'Jan':'Janauary',
		'Feb':'February',
		'Mar':'March',
		'Apr':'April',
		'May':'May',
		'Jun':'June',
		'Jul':'July',
		'Aug':'August',
		'Sep':'September',
		'Cot':'October',
		'Nov':'November',
		'Dec':'December',
}
print(monthConversions["Sep"])
print(monthConversions.get("Dec", "Not a valid key"))

guesse_word = False

print(not(guesse_word))