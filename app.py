# ============================================
# COMPLETE SCHEDULE IMPORTER - ALL SUBJECTS
# Add this to your app.py (replace the import_schedules function)
# ============================================

def import_schedules():
    """Import COMPLETE schedules for all three exams"""
    
    print("📚 Importing complete schedules...")
    
    # ========================================
    # RBI GRADE B - COMPLETE SCHEDULE
    # ========================================
    
    rbi_schedule = {
        # ----- MANAGEMENT (Days 1-48) -----
        "Management": [
            {"days": "1-3", "topic": "Motivation - Part 1"},
            {"days": "4-6", "topic": "Motivation - Part 2"},
            {"days": "8-9", "topic": "Communication"},
            {"days": "10-12", "topic": "Leadership - Part 1"},
            {"days": "13-15", "topic": "Leadership - Part 2"},
            {"days": "16-18", "topic": "General Management - Part 1"},
            {"days": "19-20", "topic": "General Management - Part 2"},
            {"days": "22-24", "topic": "General Management - Part 3"},
            {"days": "25-27", "topic": "General Management - Part 4"},
            {"days": "29", "topic": "Fundamentals of Organizational Behaviour"},
            {"days": "30-32", "topic": "Personality and Perception"},
            {"days": "33-34", "topic": "Emotional Intelligence and Interpersonal Behaviour"},
            {"days": "36-37", "topic": "Conflict"},
            {"days": "38-40", "topic": "Organizational Change and Reinforcement"},
            {"days": "41", "topic": "Corporate Governance"},
            {"days": "43-44", "topic": "Corporate Governance (continued)"},
            {"days": "45-48", "topic": "Ethics"}
        ],
        
        # ----- LOGICAL REASONING (Days 1-48) -----
        "Logical_Reasoning": [
            {"days": "1-5", "topic": "Alphabetical and Alphanumerical Series"},
            {"days": "6-12", "topic": "Coding and Decoding"},
            {"days": "13-15", "topic": "Syllogism"},
            {"days": "15-18", "topic": "Syllogism (continued)"},
            {"days": "19-20", "topic": "Direction Sense"},
            {"days": "22-23", "topic": "Direction Sense (continued)"},
            {"days": "24-27", "topic": "Inequality"},
            {"days": "29-31", "topic": "Ranking and Order"},
            {"days": "32-34", "topic": "Blood Relation"},
            {"days": "36", "topic": "Blood Relation (continued)"},
            {"days": "37-41", "topic": "Seating Arrangement"},
            {"days": "43-47", "topic": "Seating Arrangement (continued)"},
            {"days": "48", "topic": "Puzzles"}
        ],
        
        # ----- FINANCE (Days 1-90) - COMPLETE -----
        "Finance": [
            {"days": "1", "topic": "Introduction to the Indian Financial System"},
            {"days": "2-3", "topic": "Time Value of Money"},
            {"days": "4-6", "topic": "Primary and Secondary Market - Bond Market"},
            {"days": "8-10", "topic": "Basics of Derivatives - FFS"},
            {"days": "11-12", "topic": "Basics of Derivatives - Options"},
            {"days": "13", "topic": "Primary and Secondary Market - Equity Market"},
            {"days": "15-16", "topic": "Primary and Secondary Market - Equity Market (continued)"},
            {"days": "17-20", "topic": "Primary and Secondary Market - Debt Market"},
            {"days": "22-23", "topic": "Primary and Secondary Market - Forex Market"},
            {"days": "24-25", "topic": "Alternate Sources of Finance"},
            {"days": "26-27", "topic": "Banking System in India - Structure and Developments"},
            {"days": "29-30", "topic": "Banking System in India - Structure and Developments (continued)"},
            {"days": "31-34", "topic": "RBI and its Functions"},
            {"days": "36-37", "topic": "Financial Institution"},
            {"days": "38-39", "topic": "Non-Banking System"},
            {"days": "40-41", "topic": "Financial Inclusion"},
            {"days": "43-44", "topic": "Development in the Digital Payment System"},
            {"days": "45-46", "topic": "Role of IT in Banking and Financial System"},
            {"days": "47-48", "topic": "Corporate Governance in Banks"},
            {"days": "50", "topic": "Global Financial System and International Banking"},
            {"days": "51-55", "topic": "Financial Risk Management"},
            {"days": "57-60", "topic": "Introduction to Basics of Accounting"},
            {"days": "61-62", "topic": "Financial Statement - Income Statement (P&L account)"},
            {"days": "64-66", "topic": "Financial Statement - Income Statement (continued)"},
            {"days": "67-69", "topic": "Financial Statement - Balance Sheet"},
            {"days": "71-73", "topic": "Financial Statement - Balance Sheet (continued)"},
            {"days": "74-75", "topic": "Financial Statement - Cash Flow"},
            {"days": "76", "topic": "Ratios Analysis"},
            {"days": "78-80", "topic": "Ratios Analysis (continued)"},
            {"days": "81-83", "topic": "Inflation"},
            {"days": "85-86", "topic": "Public Private Partnership"},
            {"days": "87-88", "topic": "Recent Developments in Global Financial System"},
            {"days": "89-90", "topic": "Descriptive Q&A on Important Reports"}
        ],
        
        # ----- QUANTITATIVE APTITUDE (Days 1-69) -----
        "Quantitative_Aptitude": [
            {"days": "1-3", "topic": "Basic Fundamentals"},
            {"days": "4", "topic": "HCF and LCM"},
            {"days": "5", "topic": "Number System"},
            {"days": "6-11", "topic": "Percentage"},
            {"days": "12-15", "topic": "Ratio and Proportion"},
            {"days": "16-20", "topic": "Profit and Loss"},
            {"days": "22-24", "topic": "Simple Interest"},
            {"days": "25-27", "topic": "Compound Interest"},
            {"days": "29-31", "topic": "Partnership"},
            {"days": "32-33", "topic": "Problem on Ages"},
            {"days": "34-37", "topic": "Average"},
            {"days": "38-41", "topic": "Time and Work"},
            {"days": "43-45", "topic": "Pipes and Cistern"},
            {"days": "46-51", "topic": "Time and Distance"},
            {"days": "52-54", "topic": "Boats and Stream"},
            {"days": "55-57", "topic": "Mixture and Alligation"},
            {"days": "58-60", "topic": "Quadratic Equation"},
            {"days": "61-62", "topic": "Number Series"},
            {"days": "64-68", "topic": "Mix Data Interpretation"},
            {"days": "69", "topic": "Probability"},
            {"days": "69", "topic": "Mensuration 2D"}
        ],
        
        # ----- GENERAL ENGLISH (Days 1-27) -----
        "General_English": [
            {"days": "1", "topic": "Part of Speech / Structure of Speech"},
            {"days": "2-3", "topic": "Subject Verb Agreement"},
            {"days": "4-5", "topic": "Noun"},
            {"days": "6", "topic": "Pronoun"},
            {"days": "8", "topic": "Verb"},
            {"days": "9-10", "topic": "Tenses"},
            {"days": "11", "topic": "Modals"},
            {"days": "12", "topic": "Conditional Sentences"},
            {"days": "13", "topic": "Preposition"},
            {"days": "15", "topic": "Complex Prepositions"},
            {"days": "16-17", "topic": "Conjunctions"},
            {"days": "18-19", "topic": "Articles"},
            {"days": "20", "topic": "Adjectives"},
            {"days": "22", "topic": "Determiners"},
            {"days": "23", "topic": "Adverbs"},
            {"days": "24", "topic": "Active Passive Voice"},
            {"days": "24", "topic": "Rearrangement - Para Jumbles"},
            {"days": "25", "topic": "Cloze Test"},
            {"days": "25", "topic": "Reading Comprehension"},
            {"days": "26", "topic": "Phrasal Verbs"},
            {"days": "26", "topic": "Idioms and Phrases"},
            {"days": "27", "topic": "Synonyms"},
            {"days": "27", "topic": "Antonyms"},
            {"days": "27", "topic": "One Word Substitution"}
        ],
        
        # ----- DESCRIPTIVE ENGLISH (Days 1-35) -----
        "Descriptive_English": [
            {"days": "1-3", "topic": "Essay Writing"},
            {"days": "4-6", "topic": "Precis Writing"},
            {"days": "8-10", "topic": "Reading Comprehension"},
            {"days": "11-13", "topic": "Practice"},
            {"days": "15-20", "topic": "Practice (continued)"},
            {"days": "22-27", "topic": "Practice - Newspaper Editorials"},
            {"days": "29-34", "topic": "Practice - Essay Writing"}
        ],
        
        # ----- ECONOMIC AND SOCIAL ISSUES (Days 1-42) -----
        "Economic_and_Social_Issues": [
            {"days": "1-4", "topic": "Measurement of Growth"},
            {"days": "5", "topic": "Poverty Alleviation and Employment Generation"},
            {"days": "6-8", "topic": "Sustainable Development and Environmental Issues"},
            {"days": "9-11", "topic": "Economic History of India"},
            {"days": "12-17", "topic": "Fiscal Policy since Reforms of 1991"},
            {"days": "18-22", "topic": "Monetary Policy since the Reforms of 1991"},
            {"days": "23-25", "topic": "Opening up of the Indian Economy, Balance of Payments"},
            {"days": "26-27", "topic": "International Economic Institutions"},
            {"days": "29", "topic": "Regional Economic Cooperation"},
            {"days": "30-31", "topic": "Industrial and Labour Policy, Industrial Development"},
            {"days": "32", "topic": "Indian Agriculture"},
            {"days": "32", "topic": "Services Sector in India"},
            {"days": "33", "topic": "Export Import Policy"},
            {"days": "34", "topic": "International Economic Issues"},
            {"days": "34", "topic": "Economic Survey and Union Budget"},
            {"days": "36", "topic": "Multiculturalism"},
            {"days": "37", "topic": "Demographic Trends"},
            {"days": "38", "topic": "Urbanization and Migration"},
            {"days": "39", "topic": "Gender Issues"},
            {"days": "40", "topic": "Social Justice"},
            {"days": "41", "topic": "Descriptive Q&A on Important Reports"}
        ]
    }
    
    # Import RBI schedule
    for subject, topics in rbi_schedule.items():
        for topic_entry in topics:
            days_range = topic_entry['days']
            topic_name = topic_entry['topic']
            
            if '-' in str(days_range):
                start_day, end_day = map(int, str(days_range).split('-'))
            else:
                start_day = end_day = int(days_range)
            
            for day in range(start_day, min(end_day + 1, 91)):
                add_schedule_item("RBI", topic_name, day, "lecture",
                                f"Lecture: {topic_name}", 60, 1, subject)
                add_schedule_item("RBI", topic_name, day, "summary",
                                f"Summary: {topic_name}", 20, 2, subject)
                add_schedule_item("RBI", topic_name, day, "quiz",
                                f"Quiz: {topic_name}", 15, 2, subject)
    
    print("✅ RBI schedule imported")
    
    # ========================================
    # SEBI GRADE A - COMPLETE SCHEDULE
    # ========================================
    
    sebi_schedule = {
        # ----- MANAGEMENT (Days 1-55) -----
        "Management": [
            {"days": "1-3", "topic": "Motivation Part 1"},
            {"days": "4-6", "topic": "Motivation Part 2"},
            {"days": "8", "topic": "Motivation Part 2 (continued)"},
            {"days": "9-12", "topic": "Communication"},
            {"days": "13", "topic": "Leadership - Part 1"},
            {"days": "15-18", "topic": "Leadership - Part 1 (continued)"},
            {"days": "19-20", "topic": "Leadership - Part 1 (continued)"},
            {"days": "22-23", "topic": "Leadership - Part 2"},
            {"days": "24-27", "topic": "General Management - Part 1"},
            {"days": "29-32", "topic": "General Management - Part 2"},
            {"days": "33-34", "topic": "General Management - Part 3"},
            {"days": "36-37", "topic": "General Management - Part 3 (continued)"},
            {"days": "38-41", "topic": "General Management - Part 4"},
            {"days": "43-46", "topic": "HRD - Part 1"},
            {"days": "47-48", "topic": "HRD - Part 2"},
            {"days": "50-51", "topic": "HRD - Part 2 (continued)"},
            {"days": "52-54", "topic": "HRD - Part 3"}
        ],
        
        # ----- COSTING (Days 1-55) -----
        "Costing": [
            {"days": "1-2", "topic": "Overview of Cost and Management Accounting"},
            {"days": "3-4", "topic": "Material Costing"},
            {"days": "5-6", "topic": "Labour Cost"},
            {"days": "8", "topic": "Labour Cost (continued)"},
            {"days": "9-11", "topic": "Overhead Costing"},
            {"days": "12", "topic": "Activity Based Costing"},
            {"days": "13", "topic": "Output Costing or Unit Costing"},
            {"days": "15-16", "topic": "Job Costing and Batch Costing"},
            {"days": "17-19", "topic": "Contract Costing"},
            {"days": "20", "topic": "Process or Operations Costing"},
            {"days": "22-24", "topic": "Process or Operations Costing (continued)"},
            {"days": "25-27", "topic": "Joint and By-Product Costing"},
            {"days": "29-30", "topic": "Service Costing or Operating Costing"},
            {"days": "31-34", "topic": "Marginal Costing"},
            {"days": "36-38", "topic": "Marginal Costing (continued)"},
            {"days": "39-41", "topic": "Standard Costing and Variance Analysis"},
            {"days": "43-45", "topic": "Standard Costing and Variance Analysis (continued)"},
            {"days": "46-50", "topic": "Budgeting"},
            {"days": "51-54", "topic": "Lean System and Innovation"},
            {"days": "55", "topic": "Combined Practice Questions"}
        ],
        
        # ----- FINANCE (Days 1-70) -----
        "Finance": [
            {"days": "1-2", "topic": "Time Value of Money"},
            {"days": "3-6", "topic": "Bonds"},
            {"days": "8-12", "topic": "Basics of Derivatives - Futures, Forwards and Swaps"},
            {"days": "13", "topic": "Basics of Derivatives - Options"},
            {"days": "15-17", "topic": "Basics of Derivatives - Options (continued)"},
            {"days": "18-20", "topic": "Primary and Secondary Market - Equity Markets"},
            {"days": "22-23", "topic": "Primary and Secondary Market - Equity Markets (continued)"},
            {"days": "24-27", "topic": "Primary and Secondary Market - Debt & Money Market"},
            {"days": "29-32", "topic": "Financial Inclusion Using Technology"},
            {"days": "33-34", "topic": "Alternate Sources of Finance"},
            {"days": "36", "topic": "Alternate Sources of Finance (continued)"},
            {"days": "37-38", "topic": "Public Private Partnership"},
            {"days": "39-41", "topic": "Forex Markets"},
            {"days": "43-46", "topic": "Inflation"},
            {"days": "47-48", "topic": "Functions of RBI"},
            {"days": "50-52", "topic": "Functions of RBI (continued)"},
            {"days": "53-55", "topic": "Financial Institutions"},
            {"days": "56-62", "topic": "Direct and Indirect Taxes and GST"},
            {"days": "62-64", "topic": "FRBM"},
            {"days": "65-67", "topic": "Finance Commission"},
            {"days": "70", "topic": "NBFC"}
        ],
        
        # ----- COMPANY LAW (Days 1-27) -----
        "Company_Law": [
            {"days": "1-3", "topic": "Companies Act - Chapter III (Prospectus & Allotment)"},
            {"days": "4-6", "topic": "Companies Act - Chapter IV (Share Capital and Debentures)"},
            {"days": "8", "topic": "Companies Act - Chapter IV (continued)"},
            {"days": "9", "topic": "Companies Act - Chapter VIII (Declaration of Dividend)"},
            {"days": "10-11", "topic": "Companies Act - Chapter X (Audit and Auditors)"},
            {"days": "12-13", "topic": "Companies Act - Chapter XI (Appointment of Directors)"},
            {"days": "15-17", "topic": "Companies Act - Chapter XI (Directors continued)"},
            {"days": "18-20", "topic": "Companies Act - Chapter XII (Board Meetings)"},
            {"days": "22-24", "topic": "Companies Act - Chapter XII (Board Meetings continued)"},
            {"days": "25-26", "topic": "Companies Act - Chapter XXVII (NCLT and NCLAT)"}
        ],
        
        # ----- ECONOMICS (Days 1-67) -----
        "Economics": [
            {"days": "1-3", "topic": "Introduction to Economics, Demand and Supply"},
            {"days": "4-6", "topic": "Elasticity of Demand & Supply"},
            {"days": "8-10", "topic": "Production, Revenue and Cost Analysis"},
            {"days": "11-13", "topic": "Market Structures - Perfect Competition & Monopoly"},
            {"days": "15-18", "topic": "Monopolistic Competition and Oligopoly"},
            {"days": "19-20", "topic": "National Income"},
            {"days": "22", "topic": "National Income (continued)"},
            {"days": "23-27", "topic": "Classical and Keynesian Approach"},
            {"days": "29-32", "topic": "Consumption & Investment Function"},
            {"days": "33-34", "topic": "Supply and Demand for Money"},
            {"days": "43-44", "topic": "IS-LM Model"},
            {"days": "45-48", "topic": "Inflation and Phillips Curve"},
            {"days": "50-52", "topic": "Business Cycle"},
            {"days": "53-58", "topic": "Balance of Payments"},
            {"days": "59-62", "topic": "Monetary Policy"},
            {"days": "64-67", "topic": "Fiscal Policy"}
        ],
        
        # ----- COMMERCE AND ACCOUNTANCY (Days 1-83) -----
        "Commerce_and_Accountancy": [
            {"days": "1-2", "topic": "Introduction to Accounting"},
            {"days": "3-4", "topic": "Theory Base of Accounting"},
            {"days": "5-6", "topic": "Recording Transactions - Part 1"},
            {"days": "8-9", "topic": "Recording Transactions - Part 1 (continued)"},
            {"days": "10-13", "topic": "Trial Balance"},
            {"days": "15-17", "topic": "Bills of Exchange"},
            {"days": "18-22", "topic": "Income Statement"},
            {"days": "23-29", "topic": "Balance Sheet"},
            {"days": "30-33", "topic": "Ratio Analysis"},
            {"days": "34", "topic": "Cash Flow"},
            {"days": "36-41", "topic": "Accounting Transactions for Share Capital"},
            {"days": "43-45", "topic": "Accounting for Bonus Shares and Rights Issue"},
            {"days": "46", "topic": "Accounting for ESOPs"},
            {"days": "47-50", "topic": "Accounting for Buyback of Shares"},
            {"days": "51-52", "topic": "Introduction to Accounting Standards"},
            {"days": "53-55", "topic": "Accounting Standard for Inventories"},
            {"days": "57-58", "topic": "Accounting Standards for Revenue Recognition"},
            {"days": "58-61", "topic": "Accounting Standard for Foreign Transactions"},
            {"days": "62-63", "topic": "Accounting Standard for Property, Plant & Equipment"},
            {"days": "64-69", "topic": "Accounting Standard For Investment"},
            {"days": "71-76", "topic": "Preparation of Final Company Accounts"},
            {"days": "78-80", "topic": "Financial Statement Analysis"},
            {"days": "81-82", "topic": "Accounting as Financial Information System"},
            {"days": "83", "topic": "Combined Questions"}
        ],
        
        # ----- LOGICAL REASONING (Days 1-56) -----
        "Logical_Reasoning": [
            {"days": "1-2", "topic": "Alphabetical and Alphanumerical Series"},
            {"days": "3-4", "topic": "Coding and Decoding"},
            {"days": "5-6", "topic": "Syllogism"},
            {"days": "8-9", "topic": "Direction Sense"},
            {"days": "10-11", "topic": "Inequality"},
            {"days": "12-13", "topic": "Ranking and Order"},
            {"days": "15-17", "topic": "Blood Relation"},
            {"days": "18-20", "topic": "Seating Arrangement"},
            {"days": "22-26", "topic": "Puzzles"},
            {"days": "27", "topic": "Input Output"},
            {"days": "43", "topic": "Quadratic Equation"},
            {"days": "44-46", "topic": "Number Series"},
            {"days": "47-48", "topic": "Mix Data Interpretation"},
            {"days": "52-53", "topic": "Probability"},
            {"days": "54", "topic": "Mensuration 2D"},
            {"days": "55", "topic": "Mensuration 3D"}
        ],
        
        # ----- QUANTITATIVE APTITUDE (Days 1-56) -----
        "Quantitative_Aptitude": [
            {"days": "1-3", "topic": "Basic Fundamentals"},
            {"days": "4", "topic": "HCF and LCM"},
            {"days": "5", "topic": "Number System"},
            {"days": "6-10", "topic": "Percentage"},
            {"days": "11-13", "topic": "Ratio and Proportion"},
            {"days": "15-18", "topic": "Profit and Loss"},
            {"days": "19", "topic": "Simple Interest"},
            {"days": "20-22", "topic": "Compound Interest"},
            {"days": "23-24", "topic": "Partnership"},
            {"days": "25-26", "topic": "Problem on Ages"},
            {"days": "27", "topic": "Average"},
            {"days": "29-33", "topic": "Time and Work"},
            {"days": "34", "topic": "Pipes and Cistern"},
            {"days": "35-38", "topic": "Time and Distance"},
            {"days": "39-40", "topic": "Boats and Stream"},
            {"days": "41", "topic": "Quadratic Equation"}
        ],
        
        # ----- GENERAL ENGLISH (Days 1-27) -----
        "General_English": [
            {"days": "1", "topic": "Part of Speech / Structure of Speech"},
            {"days": "2-3", "topic": "Subject Verb Agreement"},
            {"days": "4-5", "topic": "Noun"},
            {"days": "6", "topic": "Pronoun"},
            {"days": "8", "topic": "Verb"},
            {"days": "9-10", "topic": "Tenses"},
            {"days": "11", "topic": "Modals"},
            {"days": "12", "topic": "Conditional Sentences"},
            {"days": "13", "topic": "Preposition"},
            {"days": "15", "topic": "Complex Prepositions"},
            {"days": "16-17", "topic": "Conjunctions"},
            {"days": "18-19", "topic": "Articles"},
            {"days": "20", "topic": "Adjectives"},
            {"days": "22", "topic": "Determiners"},
            {"days": "23", "topic": "Adverbs"},
            {"days": "24", "topic": "Active Passive Voice"},
            {"days": "24", "topic": "Rearrangement - Para Jumbles"},
            {"days": "25", "topic": "Cloze Test"},
            {"days": "25", "topic": "Reading Comprehension"},
            {"days": "26", "topic": "Phrasal Verbs"},
            {"days": "26", "topic": "Idioms and Phrases"},
            {"days": "27", "topic": "Synonyms, Antonyms & Vocabulary"}
        ],
        
        # ----- DESCRIPTIVE ENGLISH (Days 1-13) -----
        "Descriptive_English": [
            {"days": "1-3", "topic": "Essay Writing"},
            {"days": "4-6", "topic": "Precis Writing"},
            {"days": "8-10", "topic": "Reading Comprehension"},
            {"days": "11-13", "topic": "Practice"}
        ]
    }
    
    # Import SEBI schedule
    for subject, topics in sebi_schedule.items():
        for topic_entry in topics:
            days_range = topic_entry['days']
            topic_name = topic_entry['topic']
            
            if '-' in str(days_range):
                start_day, end_day = map(int, str(days_range).split('-'))
            else:
                start_day = end_day = int(days_range)
            
            for day in range(start_day, min(end_day + 1, 91)):
                add_schedule_item("SEBI", topic_name, day, "lecture",
                                f"Lecture: {topic_name}", 60, 1, subject)
                add_schedule_item("SEBI", topic_name, day, "summary",
                                f"Summary: {topic_name}", 20, 2, subject)
                add_schedule_item("SEBI", topic_name, day, "quiz",
                                f"Quiz: {topic_name}", 15, 2, subject)
    
    print("✅ SEBI schedule imported")
    
    # ========================================
    # NABARD GRADE A - COMPLETE SCHEDULE
    # ========================================
    
    nabard_schedule = {
        # ----- AGRICULTURE AND RURAL DEVELOPMENT (Days 1-69) -----
        "Agriculture_and_Rural_Development": [
            {"days": "1-2", "topic": "Introduction to Agriculture"},
            {"days": "2-6", "topic": "Agronomy"},
            {"days": "8-12", "topic": "Farming System"},
            {"days": "13", "topic": "Cropping System and Pattern"},
            {"days": "15-18", "topic": "Agrometeorology"},
            {"days": "19-20", "topic": "Seeds and Sowing"},
            {"days": "22-27", "topic": "Soil and Water Conservation"},
            {"days": "29-31", "topic": "Soil and Water Conservation (continued)"},
            {"days": "32-34", "topic": "Water Resources and Irrigation Management"},
            {"days": "36-40", "topic": "Farm and Agriculture Engineering"},
            {"days": "41", "topic": "Plantation and Horticultural Crop"},
            {"days": "43-45", "topic": "Plantation and Horticultural Crop (continued)"},
            {"days": "46-48", "topic": "Animal Husbandry and Poultry"},
            {"days": "50-51", "topic": "Animal Husbandry and Poultry (continued)"},
            {"days": "52-55", "topic": "Fisheries"},
            {"days": "57-59", "topic": "Forestry"},
            {"days": "61", "topic": "Agriculture Extension"},
            {"days": "62", "topic": "Agriculture Economics"},
            {"days": "64-65", "topic": "Ecology and Climatic Change"},
            {"days": "66-68", "topic": "Rural Development"},
            {"days": "69", "topic": "Agricultural Challenges"}
        ],
        
        # ----- LOGICAL REASONING (Days 1-56) -----
        "Logical_Reasoning": [
            {"days": "1-5", "topic": "Alphabetical and Alphanumerical Series"},
            {"days": "6-10", "topic": "Coding and Decoding"},
            {"days": "11-15", "topic": "Syllogism"},
            {"days": "16-19", "topic": "Direction Sense"},
            {"days": "20-22", "topic": "Inequality"},
            {"days": "23-24", "topic": "Ranking and Order"},
            {"days": "25-27", "topic": "Blood Relation"},
            {"days": "29-34", "topic": "Seating Arrangement"},
            {"days": "36-41", "topic": "Puzzles (continued)"},
            {"days": "43-47", "topic": "Puzzles"},
            {"days": "48", "topic": "Input Output"},
            {"days": "50", "topic": "Input Output (continued)"},
            {"days": "51", "topic": "Statement Assumption"},
            {"days": "52", "topic": "Statement Course of Action"},
            {"days": "53", "topic": "Statement Cause and Effect"},
            {"days": "54", "topic": "Statement Argument"},
            {"days": "55", "topic": "Statement and Conclusion"}
        ],
        
        # ----- QUANTITATIVE APTITUDE (Days 1-56) -----
        "Quantitative_Aptitude": [
            {"days": "1-3", "topic": "Basic Fundamentals"},
            {"days": "4", "topic": "HCF and LCM"},
            {"days": "5", "topic": "Number System"},
            {"days": "6-9", "topic": "Percentage"},
            {"days": "10-12", "topic": "Ratio and Proportion"},
            {"days": "13", "topic": "Profit and Loss"},
            {"days": "15-19", "topic": "Profit and Loss (continued)"},
            {"days": "20-23", "topic": "Compound Interest"},
            {"days": "24-25", "topic": "Partnership"},
            {"days": "26-27", "topic": "Problem on Ages"},
            {"days": "29", "topic": "Average"},
            {"days": "30-33", "topic": "Time and work"},
            {"days": "34", "topic": "Pipes and Cistern"},
            {"days": "36-40", "topic": "Time and Distance"},
            {"days": "41", "topic": "Boats and Stream"},
            {"days": "43-44", "topic": "Mixture and Alligation"},
            {"days": "45-47", "topic": "Quadratic Equation"},
            {"days": "48", "topic": "Number series"},
            {"days": "50", "topic": "Number series (continued)"},
            {"days": "51-55", "topic": "Mix data interpretation"}
        ],
        
        # ----- GENERAL ENGLISH (Days 1-13) -----
        "General_English": [
            {"days": "1", "topic": "Part of Speech / Structure of Speech"},
            {"days": "2-3", "topic": "Subject Verb Agreement"},
            {"days": "4-5", "topic": "Noun"},
            {"days": "6", "topic": "Verb and Tenses"},
            {"days": "8", "topic": "Verb and Tenses (continued)"},
            {"days": "9", "topic": "Modals"},
            {"days": "10", "topic": "Conditional Sentences"},
            {"days": "11", "topic": "Preposition and Complex Prepositions"},
            {"days": "12", "topic": "Conjunctions"},
            {"days": "13", "topic": "Adjectives, Determiners, Adverbs"},
            {"days": "13", "topic": "Rearrangement - Para Jumbles"},
            {"days": "13", "topic": "Cloze Test"},
            {"days": "13", "topic": "Reading Comprehension"},
            {"days": "13", "topic": "New Types of Questions"}
        ],
        
        # ----- COMPUTER KNOWLEDGE AND DECISION MAKING (Days 1-20) -----
        "Computer_Knowledge_and_Decision_Making": [
            {"days": "1-6", "topic": "Computer Knowledge"},
            {"days": "8-13", "topic": "Computer Knowledge (continued)"},
            {"days": "15-16", "topic": "Computer Knowledge (continued)"},
            {"days": "17-20", "topic": "Decision Making"}
        ],
        
        # ----- ECONOMIC AND SOCIAL ISSUES (Days 1-27) -----
        "Economic_and_Social_Issues": [
            {"days": "1-3", "topic": "Growth and Development"},
            {"days": "4", "topic": "Poverty Alleviation and Employment Generation"},
            {"days": "5", "topic": "Sustainable Development and Environmental Issues"},
            {"days": "6", "topic": "Economic History - Globalisation and Privatisation"},
            {"days": "8-9", "topic": "Fiscal Policy"},
            {"days": "10-12", "topic": "Monetary Policy"},
            {"days": "13", "topic": "Opening up of the Indian Economy, Balance of Payments"},
            {"days": "15", "topic": "Opening up of the Indian Economy (continued)"},
            {"days": "16", "topic": "International Economic Institutions - IMF, World Bank, WTO"},
            {"days": "17", "topic": "Regional Economic Cooperation"},
            {"days": "18", "topic": "Industrial and Labour Policy"},
            {"days": "19", "topic": "Indian Agriculture"},
            {"days": "20-21", "topic": "Inflation"},
            {"days": "22", "topic": "Multiculturalism"},
            {"days": "22", "topic": "Demographic Trends"},
            {"days": "23", "topic": "Urbanization and Migration"},
            {"days": "23", "topic": "Gender Issues"},
            {"days": "24", "topic": "Social Justice"},
            {"days": "24", "topic": "Social Movements"},
            {"days": "25", "topic": "Human Development"},
            {"days": "26", "topic": "Social Sectors - Health and Education"},
            {"days": "26", "topic": "Rural Banking and Financial Institutions"},
            {"days": "27", "topic": "Indian Political System"}
        ],
        
        # ----- DESCRIPTIVE ENGLISH (Days 1-6) -----
        "Descriptive_English": [
            {"days": "1-2", "topic": "Essay Writing"},
            {"days": "3-4", "topic": "Precis Writing"},
            {"days": "5-6", "topic": "Letter Writing"}
        ]
    }
    
    # Import NABARD schedule
    for subject, topics in nabard_schedule.items():
        for topic_entry in topics:
            days_range = topic_entry['days']
            topic_name = topic_entry['topic']
            
            if '-' in str(days_range):
                start_day, end_day = map(int, str(days_range).split('-'))
            else:
                start_day = end_day = int(days_range)
            
            for day in range(start_day, min(end_day + 1, 181)):
                add_schedule_item("NABARD", topic_name, day, "lecture",
                                f"Lecture: {topic_name}", 60, 1, subject)
                add_schedule_item("NABARD", topic_name, day, "summary",
                                f"Summary: {topic_name}", 20, 2, subject)
                add_schedule_item("NABARD", topic_name, day, "quiz",
                                f"Quiz: {topic_name}", 15, 2, subject)
    
    print("✅ NABARD schedule imported")
    print("🎉 ALL SCHEDULES IMPORTED COMPLETELY!")
    print(f"   - RBI: {len(rbi_schedule)} subjects")
    print(f"   - SEBI: {len(sebi_schedule)} subjects")
    print(f"   - NABARD: {len(nabard_schedule)} subjects")