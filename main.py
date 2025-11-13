from pyscript import display, document

def general_weighted_average(e): 
    e.preventDefault()  # prevents form from submitting

    # Get name of the student
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()

    # Get grade of each subject
    science = float(document.getElementById("science").value)
    math = float(document.getElementById("math").value)
    english = float(document.getElementById("english").value)
    filipino = float(document.getElementById("filipino").value)
    ict = float(document.getElementById("ict").value)
    pe = float(document.getElementById("pe").value)

    # Subject names
    subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]

    # Compute the GWA
    total_units = (5 * 3) + 3 + 2 + 1
    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    gwa = weighted_sum / total_units

    # summary
    summary = f"""\
{subjects[0]}: {science:.0f}
{subjects[1]}: {math:.0f}
{subjects[2]}: {english:.0f}
{subjects[3]}: {filipino:.0f}
{subjects[4]}: {ict:.0f}
{subjects[5]}: {pe:.0f}
"""

    # Display outputs
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
    
    document.getElementById("student_info").innerHTML = f"Name: {first_name} {last_name}"
    document.getElementById("summary").innerHTML = summary
    document.getElementById("output").innerHTML = f"Your general weighted average is <strong>{gwa:.2f}</strong>"
    
    
