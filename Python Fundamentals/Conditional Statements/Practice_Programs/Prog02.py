# Wap to find out whether a student has passed or failed if it requires a total of 40% .
# Assume 3 subjects and take marks as an input from the user

sub1=int(input("enter the marks of subject 1:"))
sub2=int(input("enter the marks of subject 2:"))
sub3=int(input("enter the marks of subject 3:"))
total_marks=sub1+sub2+sub3
percentage=(total_marks/300)*100
if percentage>=40:
    print("student has passed")
else:
    print("student has failed")