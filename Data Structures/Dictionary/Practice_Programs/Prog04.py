# Given subject marks in a dict, find average marks.

sub_marks={
    "English":90,
    "Hindi":98,
    "Science":89,
    "Maths":95
}

total_marks=0

for marks in sub_marks.values():
    total_marks+=marks

average=total_marks/len(sub_marks)

print("average marks of a student is:",average)