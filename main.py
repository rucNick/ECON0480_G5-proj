import pandas as pd
import matplotlib.pyplot as plt
import csv

def gdpPlot():
    df1 = pd.read_csv('chinagdp.csv')  # Replace with your first CSV file path
    df2 = pd.read_csv('usgdp.csv')  # Replace with your second CSV file path
    df3 = pd.read_csv('ukgdp.csv')  # Replace with your third CSV file path

    # Make sure the DATE column is parsed as datetime type
    df1['DATE'] = pd.to_datetime(df1['DATE'])
    df2['DATE'] = pd.to_datetime(df2['DATE'])
    df3['DATE'] = pd.to_datetime(df3['DATE'])

    # Set the DATE column as the index for each dataframe
    df1.set_index('DATE', inplace=True)
    df2.set_index('DATE', inplace=True)
    df3.set_index('DATE', inplace=True)

    # Plot the time-series data
    plt.figure(figsize=(10, 6))  # Adjust figure size as needed
    plt.plot(df1.index, df1.iloc[:, 0], label='China')  # Replace 'Dataset 1' with an appropriate label
    plt.plot(df2.index, df2.iloc[:, 0], label='United States')  # Replace 'Dataset 2' with an appropriate label
    plt.plot(df3.index, df3.iloc[:, 0], label='United Kingdom')  # Replace 'Dataset 3' with an appropriate label

    plt.title('GDP Per Capita for Countries')  # Adjust title as needed
    plt.xlabel('Year')  # Adjust x-axis label as needed
    plt.ylabel('GDP per Capita')  # Adjust y-axis label as needed
    plt.legend()
    plt.show()

def filterCsv():
    file_path = 'full_data.csv'  # Replace with your actual file path
    data = pd.read_csv(file_path)

    # Filter the dataframe
    filtered_data = data[data['location'].isin(['China', 'United States', 'United Kingdom'])]

    # Save the filtered data to a new CSV file
    filtered_file_path = 'filtered_output_file.csv'  # Define your desired output file path
    filtered_data.to_csv(filtered_file_path, index=False)

    print(f"Filtered data saved to {filtered_file_path}")

def main():
    # filterCsv()
    # gdpPlot()

main()