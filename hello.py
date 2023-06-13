import pandas as pd 
def gender():
    # Load the dataset
    gender_data = pd.read_csv("gender.csv")

    # Create a range slider for year selection
    # year_range = st.slider("Select year range", 2000, 2020, (2000, 2020))
    year_range = (2000, 2020)

    # Filter the dataset based on selected years
    filtered_data = gender_data[
        (gender_data["Year"] >= year_range[0]) & (gender_data["Year"] <= year_range[1])
    ]

    # Remove rows with NaN values in the 'Population (historical estimates)' column
    filtered_data = filtered_data.dropna(subset=["Population (historical estimates)"])

    # Exclude the entity "World" from the filtered data
    filtered_data = filtered_data[filtered_data["Entity"] != "World"]
    print(filtered_data)
    print(filtered_data.dtypes)
    agg_data = filtered_data.groupby(["Entity"])[["Population (historical estimates)", "Prevalence of current tobacco use, females (% of female adults)", "Prevalence of current tobacco use, males (% of male adults)"]].mean().reset_index()
    print(agg_data)
    # print(filtered_data.Entity.unique())

    # Aggregate the data by taking the average smoking percentages and population for each country
    # print(filtered_data.Entity.unique())
    # print(type(filtered_data.Entity))
    
    # print(agg_data)
    # print(type(agg_data))
    # print(agg_data)
    

    # agg_data2 = agg_data.mean().reset_index()

    # # Function to filter countries by region
    # def filter_countries(data, region):
    #     if region == "mena":
    #         mena_countries = [
    #             "Bahrain",
    #             "Cyprus",
    #             "Egypt",
    #             "Iran",
    #             "Iraq",
    #             "Israel",
    #             "Jordan",
    #             "Kuwait",
    #             "Lebanon",
    #             "Libya",
    #             "Morocco",
    #             "Oman",
    #             "Palestine",
    #             "Qatar",
    #             "Saudi Arabia",
    #             "Syria",
    #             "Tunisia",
    #             "Turkey",
    #             "United Arab Emirates",
    #             "Yemen",
    #         ]
    #         return data[data["Entity"].isin(mena_countries)]
    #     else:
    #         return data


if __name__ == "__main__":
    gender()