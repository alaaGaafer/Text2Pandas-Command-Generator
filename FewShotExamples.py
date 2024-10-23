few_shot_examples = [
    # Filtering
    {
        "query": "Get all rows where the salary is greater than 50000.",
        "command": "df[df['salary'] > 50000]"
    },
    # Aggregating
    {
        "query": "Calculate total sales for each region.",
        "command": "df.groupby('region')['sales'].sum()"
    },
    {
        "query": "What is maximum salary for employees.",
        "command": "df['salary'].max()"
    },
    {
        "query": "What is maximum salary for employees of each departments.",
        "command": "df.groupby('department')['salary'].max()"
    },
    {
        "query": "What is highest number of holidays taken by any employee?",
        "command": "df['holidays'].max()"
    },
    {
        "query": "What is highest number of holidays taken in each department?",
        "command": "df.groupby('department')['holidays'].max()"
    },

    # Sorting
    {
        "query": "Sort dataframe by 'date' column in descending order.",
        "command": "df.sort_values(by='date', ascending=False)"
    },
    # Summarizing
    {
        "query": "Find the average age of employees in the company.",
        "command": "df['age'].mean()"
    },
    # Filtering with multiple conditions
    {
        "query": "Select rows where 'department' is 'HR' and 'salary' is greater than 40000.",
        "command": "df[(df['department'] == 'HR') & (df['salary'] > 40000)]"
    },
    # Aggregating with multiple functions
    {
        "query": "Get the maximum and minimum salary for each department.",
        "command": "df.groupby('department')['salary'].agg(['max', 'min'])"
    },
    # Sorting with multiple columns
    {
        "query": "Sort the dataframe first by 'department' and then by 'salary' in ascending order.",
        "command": "df.sort_values(by=['department', 'salary'])"
    },
    # Summarizing with groupby
    {
        "query": "Compute the average sales for each product category, excluding categories with less than 100 sales.",
        "command": "df.groupby('product_category').filter(lambda x: x['sales'].sum() > 100).groupby('product_category')['sales'].mean()"
    },
    # Max with conditions
    {
        "query": "What is the maximum salary for employees in the 'Engineering' department?",
        "command": "df[df['department'] == 'Engineering']['salary'].max()"
    },
    {
        "query": "What is the maximum salary for employees in each region?",
        "command": "df.groupby('region')['salary'].max()"
    },
    # Multiple aggregations
    {
        "query": "What are the average and total sales for each product category?",
        "command": "df.groupby('product_category')['sales'].agg(['mean', 'sum'])"
    },
    # Filtering and then aggregating
    {
        "query": "Find the average salary for employees who have been with the company for more than 5 years.",
        "command": "df[df['years_with_company'] > 5]['salary'].mean()"
    },
    # Sorting with conditions
    {
        "query": "Sort the employees in the 'Sales' department by salary in descending order.",
        "command": "df[df['department'] == 'Sales'].sort_values(by='salary', ascending=False)"
    },
    # Conditional summarization
    {
        "query": "Calculate the average sales for 'Electronics' products only if the total sales are above 5000.",
        "command": "df[df['product_category'] == 'Electronics'].groupby('product_category').filter(lambda x: x['sales'].sum() > 5000)['sales'].mean()"
    }
]
