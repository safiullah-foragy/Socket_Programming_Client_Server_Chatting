"""
University database with public universities in Bangladesh
Contains name, short form, location, and other details
"""

UNIVERSITIES = {
    "DU": {
        "name": "University of Dhaka",
        "short": "DU",
        "location": "Dhaka-1000, Bangladesh",
        "district": "Dhaka",
        "division": "Dhaka",
        "established": "1921",
        "type": "Public University",
        "website": "www.du.ac.bd",
        "contact": "+880-2-9661900"
    },
    "BUET": {
        "name": "Bangladesh University of Engineering and Technology",
        "short": "BUET",
        "location": "Palashi, Dhaka-1000, Bangladesh",
        "district": "Dhaka",
        "division": "Dhaka",
        "established": "1962",
        "type": "Public University",
        "website": "www.buet.ac.bd",
        "contact": "+880-2-9665650"
    },
    "CU": {
        "name": "University of Chittagong",
        "short": "CU",
        "location": "Chittagong-4331, Bangladesh",
        "district": "Chittagong",
        "division": "Chittagong",
        "established": "1966",
        "type": "Public University",
        "website": "www.cu.ac.bd",
        "contact": "+880-31-2606001"
    },
    "RU": {
        "name": "University of Rajshahi",
        "short": "RU",
        "location": "Rajshahi-6205, Bangladesh",
        "district": "Rajshahi",
        "division": "Rajshahi",
        "established": "1953",
        "type": "Public University",
        "website": "www.ru.ac.bd",
        "contact": "+880-721-750041"
    },
    "RUET": {
        "name": "Rajshahi University of Engineering & Technology",
        "short": "RUET",
        "location": "Kazla, Rajshahi-6204, Bangladesh",
        "district": "Rajshahi",
        "division": "Rajshahi",
        "established": "1964",
        "type": "Public University",
        "website": "www.ruet.ac.bd",
        "contact": "+880-721-750105"
    },
    "CUET": {
        "name": "Chittagong University of Engineering & Technology",
        "short": "CUET",
        "location": "Raozan, Chittagong-4349, Bangladesh",
        "district": "Chittagong",
        "division": "Chittagong",
        "established": "1968",
        "type": "Public University",
        "website": "www.cuet.ac.bd",
        "contact": "+880-31-2606310"
    },
    "PSTU": {
        "name": "Patuakhali Science and Technology University",
        "short": "PSTU",
        "location": "Dumki, Patuakhali-8602, Bangladesh",
        "district": "Patuakhali",
        "division": "Barisal",
        "established": "2000",
        "type": "Public University",
        "website": "www.pstu.ac.bd",
        "contact": "+880-4427-56223"
    },
    "JU": {
        "name": "Jahangirnagar University",
        "short": "JU",
        "location": "Savar, Dhaka-1342, Bangladesh",
        "district": "Dhaka",
        "division": "Dhaka",
        "established": "1970",
        "type": "Public University",
        "website": "www.juniv.edu",
        "contact": "+880-2-7791045"
    },
    "KUET": {
        "name": "Khulna University of Engineering & Technology",
        "short": "KUET",
        "location": "Khulna-9203, Bangladesh",
        "district": "Khulna",
        "division": "Khulna",
        "established": "1967",
        "type": "Public University",
        "website": "www.kuet.ac.bd",
        "contact": "+880-41-769468"
    },
    "KU": {
        "name": "University of Khulna",
        "short": "KU",
        "location": "Khulna-9208, Bangladesh",
        "district": "Khulna",
        "division": "Khulna",
        "established": "1991",
        "type": "Public University",
        "website": "www.ku.ac.bd",
        "contact": "+880-41-731244"
    },
    "SUST": {
        "name": "Shahjalal University of Science and Technology",
        "short": "SUST",
        "location": "Sylhet-3114, Bangladesh",
        "district": "Sylhet",
        "division": "Sylhet",
        "established": "1986",
        "type": "Public University",
        "website": "www.sust.edu",
        "contact": "+880-821-713491"
    },
    "IU": {
        "name": "Islamic University",
        "short": "IU",
        "location": "Kushtia-7003, Bangladesh",
        "district": "Kushtia",
        "division": "Khulna",
        "established": "1979",
        "type": "Public University",
        "website": "www.iu.ac.bd",
        "contact": "+880-71-62051"
    },
    "BU": {
        "name": "University of Barisal",
        "short": "BU",
        "location": "Barisal-8200, Bangladesh",
        "district": "Barisal",
        "division": "Barisal",
        "established": "2011",
        "type": "Public University",
        "website": "www.bu.ac.bd",
        "contact": "+880-431-2179227"
    },
    "JnU": {
        "name": "Jagannath University",
        "short": "JnU",
        "location": "Sadarghat, Dhaka-1100, Bangladesh",
        "district": "Dhaka",
        "division": "Dhaka",
        "established": "2005",
        "type": "Public University",
        "website": "www.jnu.ac.bd",
        "contact": "+880-2-7113031"
    },
    "HSTU": {
        "name": "Hajee Mohammad Danesh Science and Technology University",
        "short": "HSTU",
        "location": "Dinajpur-5200, Bangladesh",
        "district": "Dinajpur",
        "division": "Rangpur",
        "established": "1999",
        "type": "Public University",
        "website": "www.hstu.ac.bd",
        "contact": "+880-531-61355"
    },
    "NSTU": {
        "name": "Noakhali Science and Technology University",
        "short": "NSTU",
        "location": "Noakhali-3814, Bangladesh",
        "district": "Noakhali",
        "division": "Chittagong",
        "established": "2003",
        "type": "Public University",
        "website": "www.nstu.edu.bd",
        "contact": "+880-321-61447"
    },
    "BSMRSTU": {
        "name": "Bangabandhu Sheikh Mujibur Rahman Science and Technology University",
        "short": "BSMRSTU",
        "location": "Gopalganj-8100, Bangladesh",
        "district": "Gopalganj",
        "division": "Dhaka",
        "established": "2001",
        "type": "Public University",
        "website": "www.bsmrstu.edu.bd",
        "contact": "+880-668-62696"
    },
    "MBSTU": {
        "name": "Mawlana Bhashani Science and Technology University",
        "short": "MBSTU",
        "location": "Santosh, Tangail-1902, Bangladesh",
        "district": "Tangail",
        "division": "Dhaka",
        "established": "1999",
        "type": "Public University",
        "website": "www.mbstu.ac.bd",
        "contact": "+880-921-55399"
    },
    "JUST": {
        "name": "Jashore University of Science and Technology",
        "short": "JUST",
        "location": "Jashore-7408, Bangladesh",
        "district": "Jashore",
        "division": "Khulna",
        "established": "2007",
        "type": "Public University",
        "website": "www.just.edu.bd",
        "contact": "+880-421-61199"
    },
    "BSTU": {
        "name": "Bangladesh University of Textiles",
        "short": "BSTU",
        "location": "Tejgaon, Dhaka-1208, Bangladesh",
        "district": "Dhaka",
        "division": "Dhaka",
        "established": "2010",
        "type": "Public University",
        "website": "www.butex.edu.bd",
        "contact": "+880-2-8891915"
    },
    "PUST": {
        "name": "Pabna University of Science and Technology",
        "short": "PUST",
        "location": "Pabna-6600, Bangladesh",
        "district": "Pabna",
        "division": "Rajshahi",
        "established": "2008",
        "type": "Public University",
        "website": "www.pust.ac.bd",
        "contact": "+880-731-65203"
    },
    "BSMMU": {
        "name": "Bangabandhu Sheikh Mujib Medical University",
        "short": "BSMMU",
        "location": "Shahbag, Dhaka-1000, Bangladesh",
        "district": "Dhaka",
        "division": "Dhaka",
        "established": "1998",
        "type": "Public Medical University",
        "website": "www.bsmmu.edu.bd",
        "contact": "+880-2-9664466"
    },
    "BAUET": {
        "name": "Bangladesh Army University of Engineering & Technology",
        "short": "BAUET",
        "location": "Natore-6431, Bangladesh",
        "district": "Natore",
        "division": "Rajshahi",
        "established": "2015",
        "type": "Public University",
        "website": "www.bauet.ac.bd",
        "contact": "+880-771-50320"
    },
    "BAUST": {
        "name": "Bangladesh Army University of Science and Technology",
        "short": "BAUST",
        "location": "Saidpur, Nilphamari-5310, Bangladesh",
        "district": "Nilphamari",
        "division": "Rangpur",
        "established": "2015",
        "type": "Public University",
        "website": "www.baust.edu.bd",
        "contact": "+880-5526-75676"
    }
}

def search_university(query):
    """
    Search for university by short form or full name
    Returns list of matching universities
    """
    query = query.upper().strip()
    results = []
    
    for short, data in UNIVERSITIES.items():
        # Exact match with short form
        if query == short.upper():
            results.append(data)
        # Partial match with full name
        elif query.lower() in data['name'].lower():
            results.append(data)
    
    return results

def list_all_universities():
    """Return all universities sorted by name"""
    return sorted(UNIVERSITIES.values(), key=lambda x: x['name'])

def format_university_info(uni):
    """Format university information for display"""
    info = f"🎓 {uni['name']}\n"
    info += f"Short Form: {uni['short']}\n"
    info += f"📍 Location: {uni['location']}\n"
    info += f"District: {uni['district']}, Division: {uni['division']}\n"
    info += f"📅 Established: {uni['established']}\n"
    info += f"Type: {uni['type']}\n"
    info += f"🌐 Website: {uni['website']}\n"
    info += f"📞 Contact: {uni['contact']}\n"
    return info
