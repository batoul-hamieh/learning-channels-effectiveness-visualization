import pandas as pd 

df = pd.read_csv("Data_Survey.csv")

df.drop("Timestamp", axis=1, inplace=True)

df.drop(df[df["major"] == 'Other'].index, inplace=True)

df.drop("major", axis=1, inplace=True)

df["university_name"] = df["university_name"].replace('LU', 'Public')

df["university_name"] = df["university_name"].replace(['LAU','AUB','USAL','USJ','LIU','MUBS','Jinan university','NDU'], 'Private')

df["academic_level"] = df["academic_level"].replace(['Masters','Graduate'], 'Postgraguate')

df["no_paltform_lecture_sufficient"] = 0

df["no_paltform_trust_uni_content"] = 0

df["no_paltform_prefer_structured_learning"] = 0

df["no_paltform_lack_platform_awareness"] = 0

df["no_paltform_lack_time_or_motivation"] = 0

df.loc[df["no_platform_usage"] == "I trust professors/university content more than online sources", "no_paltform_trust_uni_content"] = 1

df.loc[df["no_platform_usage"] == "Lectures already cover the material well.", "no_paltform_lecture_sufficient"] = 1

df.loc[df["no_platform_usage"] == "I prefer structured learning with a fixed schedule", "no_paltform_prefer_structured_learning"] = 1

df.loc[df["no_platform_usage"] == "I donâ€™t have enough time or motivation to use platforms", "no_paltform_lack_time_or_motivation"] = 1

df.loc[df["no_platform_usage"] == "I donâ€™t know about relevant online platforms", "no_paltform_lack_platform_awareness"] = 1

df.drop("no_platform_usage", axis=1, inplace=True)

df["others_review_topics"] = 0

df["others_learn_atOwnPace"] = 0

df["others_practice_exercises"] = 0

df["others_follow_upToDate_content"] = 0

df["others_certificate_internship"] = 0

df.loc[df["no_platform_others_reason_usage"].str.contains("To review topics they didnâ€™t fully understand",regex=False, na=False), "others_review_topics"] = 1

df.loc[df["no_platform_others_reason_usage"].str.contains("To learn at their own pace", regex=False,na=False), "others_learn_atOwnPace"] = 1

df.loc[df["no_platform_others_reason_usage"].str.contains("For practical examples or exercises",regex=False, na=False), "others_practice_exercises"] = 1

df.loc[df["no_platform_others_reason_usage"].str.contains("For up-to-date content", regex=False,na=False), "others_follow_upToDate_content"] = 1

df.loc[df["no_platform_others_reason_usage"].str.contains("To get certificates for jobs or internships",regex=False, na=False), "others_certificate_internship"] = 1

df.loc[df["no_platform_others_reason_usage"].str.contains("To clarify confusing lectures",regex=False, na=False), "others_review_topics"] = 1

df.loc[df["no_platform_others_reason_usage"].str.contains("To catch up if they missed classes",regex=False, na=False), "others_learn_atOwnPace"] = 1

df.drop("no_platform_others_reason_usage", axis=1, inplace=True)

domain_map = {
    "is_programming_course": ["Python", "Java", "C++", "R","PHP" ,"OOP", "Programming"],
    "is_computer_science_course": ["DSA", "Web"],
    "is_mathematics_course": ["Calculus", "Linear Algebra", "Discrete math"],
    "is_statistics_course": ["Statistics", "Probability"],
    "is_data_science_course": ["Database","SQL","Data Analysis", "Data Science", "Data Wrangling", "ML", "AI"]
}


for domain, keywords in domain_map.items():
    df[domain] = df["course"].apply(
    lambda x: int(any(keyword in x for keyword in keywords)) if isinstance(x, str) else 0
    )

df.drop("used_course_platform", axis=1, inplace=True)

df.drop("Comment1", axis=1, inplace=True)

df["incomplete_busy"] = 0

df["incomplete_lost_motivation"] = 0

df["incomplete_course_difficulty"] = 0

df["incomplete_unstructured_learning"] = 0

df["incomplete_better_resources"] = 0

df["others_certificate_internship"] = 0

df.loc[df["incomplete_reason"].str.contains("Lack of time / busy schedule", regex=False,na=False), "incomplete_busy"] = 1

df.loc[df["incomplete_reason"].str.contains("Losing motivation or interest",regex=False, na=False), "incomplete_lost_motivation"] = 1

df.loc[df["incomplete_reason"].str.contains("No structure or deadlines to keep me on track",regex=False, na=False), "incomplete_unstructured_learning"] = 1

df.loc[df["incomplete_reason"].str.contains("Course content did not meet my expectations / not useful", regex=False,na=False), "incomplete_lost_motivation"] = 1

df.loc[df["incomplete_reason"].str.contains("Course was boring or not engaging", regex=False,na=False), "incomplete_lost_motivation"] = 1

df.loc[df["incomplete_reason"].str.contains("Course difficulty or unclear explanations", regex=False,na=False), "incomplete_course_difficulty"] = 1

df.loc[df["incomplete_reason"].str.contains("Found better or more suitable learning resources",regex=False, na=False), "incomplete_better_resources"] = 1

df.loc[df["incomplete_reason"].str.contains("Learning independently feels difficult (no support)", regex=False,na=False), "incomplete_unstructured_learning"] = 1

df.drop("incomplete_reason", axis=1, inplace=True)

df["platform_review_topics"] = 0

df["platform_learn_atOwnPace"] = 0

df["platform_practice_exercises"] = 0

df["platform_upToDate_content"] = 0

df["platform_certificate_internship"] = 0

df.loc[df["platform_usage_reason"].str.contains("University courses are too theoretical", regex=False,na=False), "platform_practice_exercises"] = 1

df.loc[df["platform_usage_reason"].str.contains("Online content is more up-to-date or easier to understand",regex=False, na=False), "platform_upToDate_content"] = 1

df.loc[df["platform_usage_reason"].str.contains("Online platforms offer practical projects and hands-on skills", regex=False,na=False), "platform_practice_exercises"] = 1

df.loc[df["platform_usage_reason"].str.contains("I don't understand it from my doctor's/professor's explanation", regex=False,na=False), "platform_review_topics"] = 1

df.loc[df["platform_usage_reason"].str.contains("I prefer learning at my own pace", regex=False,na=False), "platform_learn_atOwnPace"] = 1

df.loc[df["platform_usage_reason"].str.contains("I work or have time constraints and cannot always attend classes", regex=False,na=False), "platform_learn_atOwnPace"] = 1

df.loc[df["platform_usage_reason"].str.contains("Certificates help me in job or internship applications", regex=False,na=False), "platform_certificate_internship"] = 1

df.drop("platform_usage_reason", axis=1, inplace=True)

df.drop("recommendation", axis=1, inplace=True)

df.drop("Comment2", axis=1, inplace=True)

columns_to_convert = ['used_platform', 'platform_course_completed'] 
df[columns_to_convert] = df[columns_to_convert].replace({'Yes': 1, 'No': 0})

df.dropna(how="all", inplace=True)

df.drop_duplicates(inplace=True)

df.to_csv("cleaned_responses.csv", index=False)
