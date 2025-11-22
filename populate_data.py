import sys
sys.path.append('app')
from database import insert_result
import random

# Student data with ID and Name
students = [
    ("2102002", "RUSNI AKTER"),
    ("2102003", "MD. ABU TAHER"),
    ("2102004", "MD. ABDULLAH AL MAMUN"),
    ("2102005", "MD. KAMRUZZAMAN"),
    ("2102006", "UDITA SARKAR CHANDRABINDU"),
    ("2102007", "MEHEDI HASAN"),
    ("2102008", "ABDUL JOBAYER"),
    ("2102009", "MD. MAHIBULLAH HOWLADER"),
    ("2102010", "NUSRAT JAHAN MIM"),
    ("2102012", "AISHWARIYA SARDER"),
    ("2102013", "MAHEDI HASAN NAZMUL"),
    ("2102014", "SADIA HOMAYRA NOWSHIN"),
    ("2102015", "MD. RIADUL ISLAM MAHI"),
    ("2102016", "MD. MEHEDI HASAN"),
    ("2102017", "DURJOY DAS"),
    ("2102018", "JANNATUL MIM"),
    ("2102019", "HRIDOY CHANDRA SARKER"),
    ("2102020", "MD. SADMAN KABIR BHUIYAN"),
    ("2102021", "SADMAN HAFIZ SHUVO"),
    ("2102022", "NOSHIN NAZIA"),
    ("2102023", "MD. SENARUL ISLAM"),
    ("2102024", "MD. SHARAFAT KARIM"),
    ("2102025", "SEEMANTA SHILL"),
    ("2102026", "NAYEMA FERDOUSHI"),
    ("2102027", "MD. AFRIDI ALOM PRANTO"),
    ("2102030", "YASIN ARAFAT"),
    ("2102031", "TANVIR ANJUM RAHAT"),
    ("2102032", "ARIFUL ISLAM MASUM"),
    ("2102033", "AKASH PAUL"),
    ("2102034", "MD. AL MAMUN"),
    ("2102035", "BASUDHA SHOME"),
    ("2102036", "ABUL BASAR"),
    ("2102037", "MD. SABBIR KHAN MOYEEM"),
    ("2102038", "MD.NOUSHAD BHUIYAN"),
    ("2102039", "SUVO BISWAS"),
    ("2102040", "MAHIR ASHAB"),
    ("2102041", "OMAR FARUK TANVIR"),
    ("2102042", "MD. NAIMUR RAHMAN NAIEM"),
    ("2102043", "MD. TANVIR ISLAM"),
    ("2102044", "NAZMUS SAKIB"),
    ("2102046", "MD HAJEK ANJUM BENOY"),
    ("2102047", "PUSPITA BAIDYA"),
    ("2102048", "MD. MEHEDI HASAN MONIR"),
    ("2102049", "PROSENJIT MONDOL"),
    ("2102050", "NUR MOHAMMAD NAIM"),
    ("2102051", "MD. SAFIULLAH FARAJY"),
    ("2102052", "MOHAMMED SAKIB HASAN"),
    ("2102054", "AMIT KUMAR BARMAN"),
    ("2102055", "MST. MEHERIN JAHAN JUI"),
    ("2102056", "SANDIPTA SAHA"),
    ("2102057", "SHAID IBNA SOBHAN"),
    ("2102058", "MD. SIFAT"),
    ("2102059", "MD. ABDUL KAIYUM"),
    ("2102060", "HADIBUZZAMAN"),
    ("2102062", "MAHAJABIN AFROZ MOUSHE"),
    ("2102063", "SANZIDA ISLAM NUHA"),
    ("2102064", "MD. MOBIN HAQUE"),
    ("2102065", "IMAMUL KABIR ANAN"),
    ("2102066", "NAZMUS SAKIB"),
    ("2102067", "MOHAMMAD FARHADUL HAQUE FUAD"),
    ("2102068", "MD.NAZMUL HASAN KHOKUN"),
    ("2102069", "MD. ABDUL HAI FAHIM"),
    ("2102070", "JAHID HASAN"),
    ("2102071", "JIHADUL ISLAM"),
    ("2102072", "MD. SAFAYET HOSSAIN"),
    ("2102073", "RAGHIB AL SHAHRIAR"),
    ("2102074", "ABDULLAH"),
    ("2102075", "AFRIN JAHAN"),
    ("2102076", "JANNATUL AKIBA"),
    ("2102077", "TANJIL ISLAM"),
    ("2102078", "HRIVU SAMADDAR"),
    ("2102079", "TANMOY KUMAR DAS"),
    ("2102080", "KLINTON CHAKMA"),
    ("2002002", "MISHOUK KUMAR PAUL"),
    ("2002014", "SANJANA TASNIM PROME"),
    ("2002021", "FAKIR PROTTOY MAHMUD ADIT"),
    ("2002022", "ARUP GHOSH"),
    ("2002049", "MD. MAYNUL ISLAM"),
    ("2002060", "RAJESH BISWAS"),
    ("2002066", "ASHFIKUR RAHMAN"),
    ("2002079", "MD. TOFAIEL HUSSAIN TOTA"),
    ("2002082", "ABHINASH KUMAR SAH"),
    ("1902047", "SAAD ABU SAMI"),
    ("2002005", "MD. TASNIM FERDOUS"),
]

# College options
colleges = [
    "Dhaka University",
    "BUET",
    "Chittagong University",
    "Rajshahi University",
    "RUET",
    "CUET",
    "Jahangirnagar University",
    "North South University",
    "BRAC University",
    "IUT"
]

# Board options
boards = [
    "Dhaka",
    "Chittagong",
    "Rajshahi",
    "Comilla",
    "Sylhet",
    "Barisal",
    "Dinajpur",
    "Jessore"
]

def generate_cgpa():
    """Generate a random CGPA between 2.50 and 4.00"""
    return round(random.uniform(2.50, 4.00), 2)

print("🔄 Populating database with student records...")
print("=" * 60)

count = 0
for student_id, name in students:
    cgpa = generate_cgpa()
    college = random.choice(colleges)
    board = random.choice(boards)
    
    try:
        result_id = insert_result(
            name=f"{name} (ID: {student_id})",
            result=f"CGPA: {cgpa}",
            college=college,
            board=board
        )
        count += 1
        print(f"✅ Added: {student_id} - {name} - CGPA: {cgpa}")
    except Exception as e:
        print(f"❌ Error adding {student_id} - {name}: {e}")

print("=" * 60)
print(f"✅ Successfully added {count} student records!")
print(f"\n💡 You can now search by:")
print(f"   - Student ID (e.g., 'search 2102002')")
print(f"   - Name (e.g., 'search RUSNI' or 'find MEHEDI')")
print(f"   - List all: 'list all'")
