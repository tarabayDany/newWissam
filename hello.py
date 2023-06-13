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


def risk_factors():
    deathsby = pd.read_csv("number-of-deaths-by-risk-factor.csv")

    # renaming first row
    # Read the data into a DataFrame
    data = deathsby

    # Extract the risk factors from column names
    risk_factors = [
        title.split("Risk:")[1].split(" - Sex:")[0].strip()
        for title in data.columns[3:]
    ]

    # Update the column names with risk factors
    data.columns = data.columns[:3].tolist() + risk_factors

    # Display the modified DataFrame
    data.head()

    # Set the max_rows parameter to display fewer options in the dropdown
    pd.set_option("display.max_rows", 10)

    # Read the data into a DataFrame
    # Calculate the sum of deaths by category for each year
    sum_deaths = data.groupby(["Year", "Entity"]).sum().reset_index()

    print(sum_deaths.Year.unique())

    # Get the unique entities in the data
    entities = sum_deaths["Entity"].unique()
    print(entities)

    # Create a columns layout for slider and dropdown
    # col1, col2 = st.columns([3, 1])

    # # header
    # col1.markdown(
    #     """
    #     <div style="background-color: #800020; padding: 10px">
    #         <h2 style="color: white; font-weight: bold">What are the major risk factors causing deaths in different parts of the world?</h2>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # Create a dropdown for selecting the entity
    default_entity = "World"
    # entity_dropdown = col1.selectbox(
    #     "Entity:",
    #     ["World", "Middle East & North Africa (WB)", "Lebanon"] + entities.tolist(),
    #     index=0,
    #     key="entity_dropdown",
    # )

    # Convert the min and max year values to integers
    min_year = int(sum_deaths["Year"].min())
    max_year = int(sum_deaths["Year"].max())

    # Create a slider for selecting the year
    # year_slider = col1.slider(
    #     "Year:", min_value=min_year, max_value=max_year, value=2019
    # )

    # col2.image("pics/Smok tray 2.jpg")

    # Define a function to update the plot based on the selected year and entity
    def update_plot(year, entity):
        deaths_year_entity = sum_deaths[
            (sum_deaths["Year"] == int(year)) & (sum_deaths["Entity"] == entity)
        ].squeeze()
        deaths_year_entity = deaths_year_entity.drop(["Year", "Entity"])

        # Sort the values in ascending order
        deaths_year_entity_sorted = deaths_year_entity.sort_values(ascending=True)

        # Get the top 5 categories
        top_categories = deaths_year_entity_sorted.tail(5)
        top_categories_names = top_categories.index.tolist()

        # plt.figure(figsize=(12, 6))
        # bars = plt.barh(
        #     deaths_year_entity_sorted.index,
        #     deaths_year_entity_sorted.values,
        #     color="skyblue",
        # )
        # plt.xlabel("Number of Deaths")
        # plt.ylabel("Category")
        # plt.title("Number of Deaths by Cause for {}".format(entity))

        # # Add value labels to each bar
        # for bar in bars:
        #     width = bar.get_width()
        #     plt.text(
        #         width,
        #         bar.get_y() + bar.get_height() / 2,
        #         f"{width:,}",
        #         ha="left",
        #         va="center",
        #     )

        # # Split the screen between the graph and the top risk factors
        # col_graph, col_top = st.columns([3, 1])

        # # Display the graph in the left column
        # with col_graph:
        #     st.pyplot(plt)

        # # Clear previous top risk factors
        # col_top.empty()

        # # Display top categories in the right column
        # with col_top:
        #     st.markdown(
        #         "<h3 style='font-size: 50px;'>Top Risk Factors:</h3>",
        #         unsafe_allow_html=True,
        #     )
        #     for i, category in enumerate(reversed(top_categories_names), 1):
        #         st.markdown(
        #             f'<p style="font-size: 35px;">{i}. {category}</p>',
        #             unsafe_allow_html=True,
                # )

    # Update the plot based on the selected year and entity
    # update_plot(year_slider, entity_dropdown)



if __name__ == "__main__":
    # gender()
    risk_factors()