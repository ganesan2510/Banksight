import streamlit as st
import mysql.connector
import pandas as pd

#st.title('This is my Streamlit app')
def get_connection():
    return mysql.connector.connect(        
        host="localhost",
        user="root",
        password="Rajaram25*",
        database="banksight"
    )

def load_table(query):
    conn=get_connection()    
    df= pd.read_sql(query,conn)
    conn.close()
    return df


def delete_records(query):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SET SQL_SAFE_UPDATES = 0")
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_update_records(query,data):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SET SQL_SAFE_UPDATES = 0")
    cursor.execute(query,data)
    conn.commit()
    cursor.close()
    conn.close()

st.sidebar.title('BankSight')
menu = st.sidebar.radio(
    "Go to :",
    [
        "Introduction",
        "View Tables",
        "Filter Data",
        "CRUD Operations",
        "Credit / Debit Simulation",
        "Analytical Insights",
        "About Creator"
    ]
)

# Page routing
if menu == "Introduction":
    st.title("BankSight: Transaction Intelligence Dashboard")
    st.subheader("Project Overview")
    st.write('BankSight is a financial analytice system built using Python, Streamlit and mysql. it allows users to explore customer, account, transaction, loan, and support data, perform CURD operations, simulate deposits/withdraws and view analytical inisghts.')
    st.subheader("Objectives:")
    st.markdown("""
                - Understand customer & transaction behavior
                - Detect anomalies and potential fraud
                - Provide an interactive Streamlit app to explore transactions
                """)
    st.divider()
elif menu == "View Tables":
    st.title("View Database Tables")    
    try:
        option = st.selectbox("Select a table:", ["Accounts", "Branches","Credit_Cards", "Customers", "Loans","Support_Tickets",
                                                  "Transactions"],    index=1          )
        #st.write(option)
        query='select * from '+ option
        df_table = load_table(query)
        st.dataframe(df_table, use_container_width=True)

        #st.success(f"Loaded {len(df_customers)} customer records")

    except Exception as e:
        st.error(f"Error loading data: {e}")
    st.divider()


elif menu == "Filter Data":    
    st.title("Filter Data")
    try:        
        option = st.selectbox("Select a table to filter:", ["Accounts", "Branches","Credit_Cards", "Customers", "Loans","Support_Tickets",
                                                "Transactions"],    index=0 )
        if option == "Customers":
            df_table = load_table("SELECT customer_id FROM customers")
            customer_id_list = df_table['customer_id'].tolist()
            option = st.selectbox(    "Customer_id:",    customer_id_list,    index=0  )
            query="select * from customers where Customer_id='"+ option+"'"
            df_table = load_table(query)
            st.dataframe(df_table, use_container_width=True)
        elif option == "Accounts":
            df_table = load_table("SELECT customer_id FROM accounts")
            account_id_list = df_table['customer_id'].tolist()
            option = st.selectbox( "Customer_id:", account_id_list,    index=0  )
            query="select * from accounts where Customer_id='"+ option+"'"
            df_table = load_table(query)
            st.dataframe(df_table, use_container_width=True)
        elif option == "Branches":
            df_table = load_table("SELECT Branch_id FROM Branches")
            Branch_id_list = df_table['Branch_id'].tolist()
            option = st.selectbox( "Branch_id:", Branch_id_list,    index=0  )
            query="select * from Branches where Branch_id="+ str(option)
            df_table = load_table(query)
            st.dataframe(df_table, use_container_width=True)
        elif option == "Credit_Cards":
            df_table = load_table("SELECT Card_id FROM Credit_Cards")
            Card_id_list = df_table['Card_id'].tolist()
            option = st.selectbox( "Card_id:", Card_id_list,    index=0  )
            query="select * from Credit_Cards where Card_id="+ str(option)
            df_table = load_table(query)
            st.dataframe(df_table, use_container_width=True)
        elif option == "Loans":
            df_table = load_table("SELECT Loan_id FROM Loans")
            Loan_id_list = df_table['Loan_id'].tolist()
            option = st.selectbox( "Loan_id:", Loan_id_list,    index=0  )
            query="select * from Loans where Loan_id="+str( option)
            df_table = load_table(query)
            st.dataframe(df_table, use_container_width=True)
        elif option == "Support_Tickets":
            df_table = load_table("SELECT ticket_id FROM Support_Tickets")
            Loan_id_list = df_table['ticket_id'].tolist()
            option = st.selectbox( "ticket_id:", Loan_id_list,    index=0  )
            query="select * from Support_Tickets where ticket_id='"+ option+"'"
            df_table = load_table(query)
            st.dataframe(df_table, use_container_width=True)
        elif option == "Transactions":
            df_table = load_table("SELECT txn_id FROM Transactions")
            txn_id_list = df_table['txn_id'].tolist()
            option = st.selectbox( "txn_id:", txn_id_list,    index=0  )
            query="select * from Transactions where txn_id='"+ option+"'"
            df_table = load_table(query)
            st.dataframe(df_table, use_container_width=True)
            #st.success(f"Loaded {len(df_customers)} customer records")
    except Exception as e:
        st.error(f"Error loading data: {e}")
    st.divider()

elif menu == "CRUD Operations":
    st.title("CRUD Operations")    
    try:
        tablename = st.selectbox("Select a table:", ["Accounts", "Branches","Creadit_Cards", "Customers", "Loans","Support_Tickets",
                                                  "Transactions"],    index=0   )
        curd = st.radio(  "Choose :",    ["View", "Add", "Update","Delete"],horizontal=False)
        if tablename=="Accounts":
            if curd=="View":
                st.write('View Table '+tablename)
                query='select * from '+ tablename
                df_table = load_table(query)
                st.dataframe(df_table, use_container_width=True)
            elif curd=="Delete":
                st.write('Delete Record ')
                df_table = load_table("SELECT customer_id FROM accounts")
                account_id_list = df_table['customer_id'].tolist()
                option = st.selectbox( "Customer_id:", account_id_list, index=None, placeholder="Select a customer"  )
                st.write('opetion value :' + option)
                if option is None:
                    st.info("Please select a customer to view data")
                else:
                    query="delete from Accounts where Customer_id='"+ option+"'"
                    st.write('Record id '+ option+ ' is deleted')
                    delete_records(query)
            elif curd=="Add":
                st.write('Add new Record ')
                customer_id = st.text_input("Enter Customer id: ")
                account_balance = st.text_input("Enter Account Balance: ")                
                if st.button("Add New", type="secondary"):
                    query="insert into accounts (customer_id, account_balance,last_updated) values('"+customer_id+"', '"+account_balance+"',current_timestamp())"
                    st.write(query)
                    delete_records(query)
                    st.write("Record added!")
            elif curd=="Update":
                st.write('Update Record ')
                df_table = load_table("SELECT customer_id FROM accounts")
                account_id_list = df_table['customer_id'].tolist()
                customer_id = st.selectbox( "Customer_id:", account_id_list  )                
                account_balance = st.text_input("Enter Account Balance: ")                
                if st.button("Update", type="secondary"):
                    query="update accounts set account_balance = '"+account_balance+"' , last_updated = current_timestamp() where customer_id ='"+customer_id+"'"
                    delete_records(query)
                    st.write(customer_id +" Updated!")
    except Exception as e:
        st.error(f"Error loading data: {e}")
    st.divider()
elif menu == "Credit / Debit Simulation":
    st.title("Credit / Debit Amount")
    df_table = load_table("SELECT customer_id FROM accounts")
    account_id_list = df_table['customer_id'].tolist()
    customer_id = st.selectbox( "Account id:", account_id_list, index=0  )

    action=st.radio("Select Action:",["Check Balance","Deposit","Withdraw"],index=1)
    query="SELECT * FROM Accounts where customer_id='"+customer_id+"'"
    #st.write(query)
    if action=="Check Balance":
        df_table = load_table(query)
        st.success("Account balance : "+str(df_table['account_balance'][0]))
    elif action=="Deposit":
        deposit_amount = st.text_input("Enter Amount to Deposit: ",value=0)
        amount = float(deposit_amount)
        if amount > 0:            
            query="SELECT * FROM Accounts where customer_id='"+str(customer_id)+"'"
            df_table = load_table(query)
            if st.button("Click to Deposit", type="secondary"):  
                 balance = float(df_table['account_balance'].iloc[0]) + amount
                 update_query="update accounts set account_balance ="+str(balance)+" , last_updated = current_timestamp() where customer_id ='"+str(customer_id)+"'"
                 delete_records(update_query)
                 st.success("Account Updated, Current Balance: ₹"+ str(balance))
        else:
            st.error('please enter deposit amount. ')
    elif action=="Withdraw":
        withdraw_amount = st.text_input("Enter Amount to Withdraw: ",value=0)
        amount = float(withdraw_amount)
        if amount > 0:            
            query="SELECT * FROM Accounts where customer_id='"+str(customer_id)+"'"
            df_table = load_table(query)
            if st.button("CLick to Widthdraw", type="secondary"):  
                 balance = float(df_table['account_balance'].iloc[0]) - amount
                 update_query="update accounts set account_balance ="+str(balance)+" , last_updated = current_timestamp() where customer_id ='"+str(customer_id)+"'"
                 delete_records(update_query)
                 st.success("Account Updated, Current Balance: ₹"+ str(balance))
        else:
            st.error('please enter deposit amount. ')
    st.divider()
elif menu == "Analytical Insights":
    st.title("Analytical Insights")
    question = st.selectbox( "Select a Question:", 
                          [
                              "Q1: How many customers exist per city, and what is their average account balance?",
                              "Q2: Which account type (Savings, Current, Loan, etc.) holds the highest total balance?",
                              "Q3: Who are the top 10 customers by total account balance across all account types?",
                              "Q4: Which customers opened accounts in 2023 with a balance above ₹1,00,000?",
                              "Q5: What is the total transaction volume (sum of amounts) by transaction type?",
                              "Q6: How many failed transactions occurred for each transaction type?",
                              "Q7: What is the total number of transactions per transaction type?",
                              "Q8: Which accounts have 5 or more high-value transactions above ₹20,000?",
                              "Q9: What is the average loan amount and interest rate by loan type (Personal, Auto, Home, etc.)?",
                              "Q10: Which customers currently hold more than one active or approved loan?",
                              "Q11: Who are the top 5 customers with the highest outstanding (non-closed) loan amounts?",
                              "Q12: What is the average loan amount per branch?",
                              "Q13: How many customers exist in each age group (e.g., 18-25, 26-35, etc.)?",
                              "Q14: Which issue categories have the longest average resolution time?",
                              "Q15: Which support agents have resolved the most critical tickets with high customer ratings (≥4)?"
                          ], index=0  )
    if question=="Q1: How many customers exist per city, and what is their average account balance?":
        selectQuery="""SELECT c.city,count(c.name), avg(a.account_balance) FROM banksight.customers c
        join banksight.accounts a on a.customer_id=c.customer_id
        group by c.city 
        order by c.city """
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q2: Which account type (Savings, Current, Loan, etc.) holds the highest total balance?":
        selectQuery="""SELECT c.account_type, sum(a.account_balance) FROM customers c
                    JOIN accounts a ON c.customer_id = a.customer_id
                    group by c.account_type  
                    order by sum(a.account_balance) desc 
                    limit 1"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q3: Who are the top 10 customers by total account balance across all account types?":
        selectQuery="""SELECT    
                        c.customer_id, c.name, a.account_balance FROM customers c
                        JOIN accounts a ON c.customer_id = a.customer_id
                        order by a.account_balance desc
                        limit 10"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q4: Which customers opened accounts in 2023 with a balance above ₹1,00,000?":
        selectQuery="""SELECT c.customer_id,c.name,  a.account_balance  FROM customers c
                        JOIN accounts a ON c.customer_id = a.customer_id
                        where YEAR(c.join_date) = 2023 and a.account_balance>100000
                        order by a.account_balance desc """
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q5: What is the total transaction volume (sum of amounts) by transaction type?":
        selectQuery="""select txn_type,sum(amount) from banksight.transactions 
                        group by txn_type"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q6: How many failed transactions occurred for each transaction type?":
        selectQuery="""select txn_type,count(status) from banksight.transactions 
                        where status='failed'
                        group by txn_type"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q7: What is the total number of transactions per transaction type?":
        selectQuery="""select txn_type,count(status) TransactionCount from banksight.transactions 
                        group by txn_type"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q8: Which accounts have 5 or more high-value transactions above ₹20,000?":
        selectQuery="""select customer_id, count(*) from banksight.transactions where amount > 20000  
                        AND status = 'success'
                        group by customer_id HAVING COUNT(*) >= 5
                        order by count(*) desc"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q9: What is the average loan amount and interest rate by loan type (Personal, Auto, Home, etc.)?":
        selectQuery="""select Loan_Type, avg(Loan_Amount), round(avg(Interest_Rate),2) from banksight.loans
                        group by Loan_Type"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q10: Which customers currently hold more than one active or approved loan?":
        selectQuery="""select customer_id, count(*) from banksight.loans
                        where Loan_Status in ('Active','Approved')
                        group by customer_id having count(*)>1"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q11: Who are the top 5 customers with the highest outstanding (non-closed) loan amounts?":
        selectQuery="""select   customer_id, sum(Loan_Amount) from  banksight.loans  
                        where Loan_Status != 'Closed'
                        group by customer_id
                        order by sum(Loan_Amount) desc
                        limit 5"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q12: What is the average loan amount per branch?":
        selectQuery="""select Branch, count(*),avg(Loan_Amount) FROM banksight.loans
                        group by Branch order by Branch"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q13: How many customers exist in each age group (e.g., 18-25, 26-35, etc.)?":
        selectQuery="""select 
                        case 
                        WHEN age BETWEEN 18 AND 25 THEN '18-25'
                                WHEN age BETWEEN 26 AND 35 THEN '26-35'
                                WHEN age BETWEEN 36 AND 45 THEN '36-45'
                                WHEN age BETWEEN 46 AND 60 THEN '46-60'
                                ELSE '60+'
                        END AS age_group,
                        COUNT(*) AS customer_count
                        FROM banksight.customers 
                        group by age_group"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q14: Which issue categories have the longest average resolution time?":
        selectQuery=""" select Issue_Category, avg(DATEDIFF(Date_Closed,Date_Opened)) AS AvgResultion from banksight.support_tickets
                        group by Issue_Category
                        order by AvgResultion desc"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True)
    elif question=="Q15: Which support agents have resolved the most critical tickets with high customer ratings (≥4)?":
        selectQuery="""SELECT   Support_Agent,    COUNT(*) AS Count FROM banksight.support_tickets
                        WHERE Priority = 'Critical'   AND Status IN ('Closed', 'Resolved')  AND Customer_Rating >= 4
                        GROUP BY Support_Agent
                        ORDER BY Count DESC"""
        st.write('QUERY : '+selectQuery)
        df_table=load_table(selectQuery)
        st.dataframe(df_table, use_container_width=True) 
    st.divider()       
elif menu == "About Creator":
    st.title("About the Creator")
    st.markdown("""
                **Name:** Ganesan Rajagopal\n
                **Role:** .Net Developer\n
                **Expertise:** c#, HTML, CSS, Jquery.\n
                Project developed as part of the BankSight Analytics initiative to demonstrate end to end data engineering and analysis workflows.
                """)
    st.divider()
