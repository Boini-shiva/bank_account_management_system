from logging import raiseExceptions
import datetime

class Sbi:
    Bank_Name="SBI"
    Bank_Loc="Chaitanya puri"
    Ifsc_code="SBI00o456"
    Bank_Mgr="Sri"
    Pin_Code=500060

    No_Cust=0
    Cust_Details={}
    transaction_details={}

    def __init__(self,name,phone,age,aadhar,address,pin_code,pin,balance):
        self.name=name
        self.phone=self.valid_ph(phone)
        self.age=self.valid_age(age)
        self.aadhar=self.valid_aadhar(aadhar)
        self.address=address
        self.pin_code= self.valid_pin_code(pin_code)
        self.pin=self.valid_pin(pin)
        self.balance=balance

######## for the Bank pin code validation
        Sbi.Pin_Code= self.valid_pin_code(Sbi.Pin_Code)
########### calling the no.of customers method
        self.increment_no_customers()
        self.acc_no=65487421400+self.No_Cust


        # self.Cust_Details[acc_no]=self
        self.store_cust_data(self.acc_no,self)


##to generate random account number
    @classmethod
    def increment_no_customers(cls):

        cls.No_Cust +=1
        # print(Sbi.No_Cust)

##To store data
    @classmethod
    def store_cust_data(cls,acc_no,cust_data):
        cls.Cust_Details[acc_no]=cust_data


##Validate phone number
    @staticmethod
    def valid_ph(ph_no):
        if len(str(ph_no)) == 10 and str(ph_no).isdigit() :
            return ph_no
        else :
            raise Exception("Enter Valid Phone Number")

##Validate adhaar card
    # @staticmethod
    # def valid_aadhar(aadhar):
    #     if len(str(aadhar)) == 12 and str(aadhar).isdigit() and aadhar !=  Sbi.Cust_Details :
    #         return aadhar
    #     else :
    #         raise Exception("Enter Valid Aadhar Number")

    @staticmethod
    def valid_aadhar(aadhar):
        if len(str(aadhar)) == 12 and str(aadhar).isdigit() :
            return aadhar
        else :
            raise Exception("Enter Valid Aadhar Number")


##validate PIN NUMBER
    @staticmethod
    def valid_pin(pin):
        if len(str(pin)) == 4 and str(pin).isdigit() :
            return pin
        else :
            raise Exception("Enter Valid Pin Number")

##validate AGE
    @staticmethod
    def valid_age(age):
        if age>=18:
            return age
        else:
            raise Exception("you not eligible to the creating account")

##validation PIN CODE
    @staticmethod
    def valid_pin_code(pin_code):
        if len(str(pin_code)) == 6 and str(pin_code).isdigit() :
            return pin_code
        else :
            raise Exception("Enter Valid Pin Code Number")


##validation CHECK BALANCE
    @classmethod
    def dis_cust_check_balance(cls):
        print("-" * 50, "-> WELCOME TO CHECK YOUR BALANCE PAGE <-", "-" * 50)
        ac_no=int(input("Enter the account number : "))
        pin_no = int(input("Enter the pin number : "))
        if ac_no in cls.Cust_Details and pin_no == cls.Cust_Details[ac_no].pin :
            print(f"The Customer {cls.Cust_Details[ac_no].name} Current Balance is : {cls.Cust_Details[ac_no].balance}")
        elif ac_no in cls.Cust_Details and pin_no != cls.Cust_Details[ac_no].pin :
            raise Exception("Invalid Password")

        else:
            raise Exception("Invalid Credentials")

    @classmethod
    def dis_deposit_amt(cls,count=0):
        print("-"*50,"->WELCOME TO DEPOSIT PAGE <-","-"*50)
        ac_no=int(input("Enter the account number : "))
        pin_no = int(input("Enter the pin number : "))
        if count==1:
            print("YOU HAVE REACHED MAXIMUM ATTEMPTS")



        if ac_no in cls.Cust_Details and pin_no == cls.Cust_Details[ac_no].pin :
            amt=int(input("Enter the amount : "))

            if amt>0:
                cls.Cust_Details[ac_no].balance +=amt
                print(f"rs.{amt} has been credited to your account, and your current balance is {cls.Cust_Details[ac_no].balance}")

                if ac_no not in cls.transaction_details:
                    cls.transaction_details[ac_no]=[{"DATE" : datetime.datetime.now(),
                                                     "TYPE OF TRANSACTION": "CREDITED",
                                                    "TRANSACTION AMOUNT" :  amt,
                                                    "BALANCE AMOUNT" : cls.Cust_Details[ac_no].balance}]

                else :
                    cls.transaction_details[ac_no] += [{"DATE": datetime.datetime.now(),
                                                       "TYPE OF TRANSACTION": "CREDITED",
                                                       "TRANSACTION AMOUNT": amt,
                                                       "BALANCE AMOUNT": cls.Cust_Details[ac_no].balance}]



            else:
                raise Exception("Enter the Valid Amount")
        elif ac_no in cls.Cust_Details and pin_no != cls.Cust_Details[ac_no].pin :
            raise Exception("Invalid Password")
        # else:
        #     raise Exception("Invalid Credentials")
        else:

            print("Invalid Credentials")
            cls.dis_deposit_amt(count + 1)
            raise Exception("boss u have completed ur attempts")





    @classmethod
    def dis_withdraw_amt(cls):
        print("-" * 50, "->WELCOME TO WITHDRAW PAGE <-", "-" * 50)
        ac_no = int(input("Enter the account number : "))
        pin_no = int(input("Enter the pin number : "))
        if ac_no in cls.Cust_Details and pin_no == cls.Cust_Details[ac_no].pin:
            amt = int(input("Enter the amount : "))
            if amt <= cls.Cust_Details[ac_no].balance and amt >0 :
                cls.Cust_Details[ac_no].balance -= amt
                print(f"rs.{amt} has been debited to your account, and your current balance is {cls.Cust_Details[ac_no].balance}")

                if ac_no not in cls.transaction_details:
                    cls.transaction_details[ac_no] = [{"DATE": datetime.datetime.now(),
                                                       "TYPE OF TRANSACTION": "DEBITED",
                                                       "TRANSACTION AMOUNT": amt,
                                                       "BALANCE AMOUNT": cls.Cust_Details[ac_no].balance}]

                else:
                    cls.transaction_details[ac_no] += [{"DATE": datetime.datetime.now(),
                                                        "TYPE OF TRANSACTION": "DEBITED",
                                                        "TRANSACTION AMOUNT": amt,
                                                        "BALANCE AMOUNT": cls.Cust_Details[ac_no].balance}]


            elif amt>cls.Cust_Details[ac_no].balance:
                raise Exception("Insufficient balance")

            else:
                raise Exception("Enter the Valid Amount")
        elif ac_no in cls.Cust_Details and pin_no != cls.Cust_Details[ac_no].pin:
            raise Exception("Invalid Password")

        else:
            raise Exception("Invalid Credentials")


    @classmethod
    def dis_modify_pin(cls):
        print("-" * 50, "->WELCOME TO PIN MODIFICATION PAGE <-", "-" * 50)
        ac_no=int(input("Enter the account number : "))
        pin_no = int(input("Enter the pin number : "))
        if ac_no in cls.Cust_Details and pin_no == cls.Cust_Details[ac_no].pin :
            new_pin=int(input("Enter the new pin : "))
            confirm_pin=int(input("Enter the confirm pin : "))
            cls.valid_pin(new_pin)
            cls.valid_pin(confirm_pin)
            if new_pin==confirm_pin and new_pin != cls.Cust_Details[ac_no].pin:
                # cls.valid_pin(new_pin)
                # cls.valid_pin(confirm_pin)
                cls.Cust_Details[ac_no].pin=new_pin
                print("your current pin XXXX is updated to XXXX successfully ")

            elif new_pin == cls.Cust_Details[ac_no].pin and new_pin != confirm_pin :
                raise Exception("your old pin and new pin are same , use different pin which is different to the old pin and your new pin and confirm pin is not matched")


            elif new_pin != confirm_pin :
                raise Exception("your new pin and confirm pin is not matched")


            else:
                raise Exception("your old pin and new pin are same , use different pin which is different to the old pin")

        elif ac_no in cls.Cust_Details and pin_no != cls.Cust_Details[ac_no].pin :
            raise Exception("Invalid Password")

        else:
            raise Exception("Invalid Credentials")

    @classmethod
    def dis_modify_cust_data(cls):
        print("-"*50,"> WELCOME TO CUSTOMER DETAILS MODIFICATION PAGE <","-"*50)
        ac_no=int(input("Enter the account number : "))
        pin_no = int(input("Enter the pin number : "))
        if ac_no in cls.Cust_Details and pin_no == cls.Cust_Details[ac_no].pin :
            while True:
                print(f"Select 1 To Change The Name :\n"
                      f"Select 2 To Change The Phone Number :\n"
                      f"Select 3 To Change The Address :")
                select = int(input("Enter The Number To Change The Details : "))

                match select:
                    case 1 :
                        print("-" * 50, "> Welcome To Modify Name <", "-" * 50)
                        new_name=input("enter the new name")
                        confirm_name=input("enter the confirm name")

                        if new_name==confirm_name and new_name != cls.Cust_Details[ac_no].name:
                            # print("old name : ",cls.Cust_Details[ac_no].name)
                            cls.Cust_Details[ac_no].name=new_name
                            print("your name updated successfully . ")
                            print("new name :",cls.Cust_Details[ac_no].name)

                        elif new_name == cls.Cust_Details[ac_no].name:
                            raise Exception("new name and old name is must be different")

                        else :
                            raise Exception("new name and confirm name is not matches")

                    case 2 :
                        print("-" * 50, "> Welcome To Modify Phone number <", "-" * 50)
                        new_ph = int(input("enter the new phone number"))
                        confirm_ph = int(input("enter the confirm phone number"))
                        cls.valid_ph(new_ph)
                        cls.valid_ph(confirm_ph)

                        if new_ph == confirm_ph and new_ph != cls.Cust_Details[ac_no].phone :
                            # print("old phone number : ",cls.Cust_Details[ac_no].phone)
                            cls.Cust_Details[ac_no].phone = new_ph
                            print("your phone number updated successfully . ")
                            print("new name", cls.Cust_Details[ac_no].phone)

                        elif new_ph == cls.Cust_Details[ac_no].phone:
                            raise Exception("new phone number  and old phone number must be different")

                        else:
                            raise Exception("new phone number and confirm phone number is not matches")

                    case 3 :
                        print("-" * 50, "> Welcome To Modify Phone number <", "-" * 50)
                        new_addr = input("enter the new address")
                        confirm_addr = input("enter the confirm address")


                        if new_addr == confirm_addr and new_addr != cls.Cust_Details[ac_no].address:
                            # print("old address : ",cls.Cust_Details[ac_no].address)
                            cls.Cust_Details[ac_no].address = new_addr
                            print("your address updated successfully . ")
                            print("new address", cls.Cust_Details[ac_no].address)

                        elif new_addr == cls.Cust_Details[ac_no].address:
                            raise Exception("new address  and old phone address must be different")

                        else:
                            raise Exception("new address and confirm address is not matches")

                    case __:
                        print("There are only three options like 1, 2, 2 .")







        elif ac_no in cls.Cust_Details and pin_no != cls.Cust_Details[ac_no].pin :

            raise Exception("Invalid Password")

        else :
            raise Exception("Invalid Credentials")

    @classmethod
    def dis_transfer_amt(cls):
        print("-" * 50, "->WELCOME TO TRANSFER AMOUNT  PAGE <-", "-" * 50)
        sender_ac_no = int(input("Enter the sender's account number : "))
        sender_pin_no = int(input("Enter the sender's pin number : "))
        if sender_ac_no in cls.Cust_Details and sender_pin_no == cls.Cust_Details[sender_ac_no].pin:
            receiver_ac_no = int(input("Enter the receiver's account number : "))
            receiver_ifsc_code = input("Enter the receiver's ifsc code : ")
            if receiver_ac_no in cls.Cust_Details and receiver_ifsc_code == cls.Ifsc_code :
                amt=int(input("enter the amount : "))
                if amt <= cls.Cust_Details[sender_ac_no].balance :
                    print("_"*50,"before transferring","_"*50)
                    print(f"The Sender balance before transferring amount is : {cls.Cust_Details[sender_ac_no].balance}")
                    print(f"The receiver balance before credited amount balance amount is : {cls.Cust_Details[receiver_ac_no].balance}")
                    cls.Cust_Details[sender_ac_no].balance -= amt
                    cls.Cust_Details[receiver_ac_no].balance += amt
                    print("_" * 50, "after transferring", "_" * 50)
                    print(f"The Sender balance after transferring amount is : {cls.Cust_Details[sender_ac_no].balance}")
                    print(f"The amount {amt} rupees credited to the receiver's bank ,now current balance amount is : {cls.Cust_Details[receiver_ac_no].balance}")


                    if sender_ac_no not in cls.transaction_details or receiver_ac_no not in cls.transaction_details:
                        cls.transaction_details[sender_ac_no] = [{"DATE": datetime.datetime.now(),
                                                           "TYPE OF TRANSACTION": "TRANSFERRED",
                                                           "TRANSACTION AMOUNT": amt,
                                                           "BALANCE AMOUNT": cls.Cust_Details[sender_ac_no].balance}]


                        cls.transaction_details[receiver_ac_no] = [{"DATE": datetime.datetime.now(),
                                                            "TYPE OF TRANSACTION": "RECEIVED",
                                                            "TRANSACTION AMOUNT": amt,
                                                            "BALANCE AMOUNT": cls.Cust_Details[receiver_ac_no].balance}]





                    else :
                        cls.transaction_details[sender_ac_no] += [{"DATE": datetime.datetime.now(),
                                                            "TYPE OF TRANSACTION": "TRANSFERRED",
                                                            "TRANSACTION AMOUNT": amt,
                                                            "BALANCE AMOUNT": cls.Cust_Details[sender_ac_no].balance}]

                        cls.transaction_details[receiver_ac_no] += [{"DATE": datetime.datetime.now(),
                                                           "TYPE OF TRANSACTION": "RECEIVED",
                                                           "TRANSACTION AMOUNT": amt,
                                                           "BALANCE AMOUNT": cls.Cust_Details[receiver_ac_no].balance}]


                else :
                    raise Exception("******you have insufficient balance*****")

            else:
                raise Exception("receiver not found")
        elif sender_ac_no in cls.Cust_Details and sender_pin_no != cls.Cust_Details[sender_ac_no].pin:
            raise Exception("Invalid Password")

        else:
            raise Exception("Invalid Credentials")

    @classmethod
    def dis_mini_stmt(cls):
        user_ac_no= int(input("enter the account number : "))
        user_pin_no= int(input("enter the pin number : "))
        if user_ac_no in cls.Cust_Details and user_pin_no == cls.Cust_Details[user_ac_no].pin :
            print("DATE_TIME".ljust(30), "TYPE_OF_TRANSACTION".ljust(45), "AMOUNT".ljust(30), "BALANCE".ljust(30))
            transaction_history = cls.transaction_details[user_ac_no]
            for d in transaction_history:
                print(str(d["DATE"]).ljust(30),d["TYPE OF TRANSACTION"].ljust(45),str(d["TRANSACTION AMOUNT"]).ljust(30),str(d["BALANCE AMOUNT"]).ljust(30))



c1=Sbi("Pavan",9392567814,24,456789487154,"dsnr",500045,4568,45000)
c2=Sbi("Vani",9192567814,22,496786872154,"uppal",500047,4567,40000)
c3=Sbi("Shivani",9198767814,23,456789487154,"kphb",500058,2564,100000)


# methods to do operations

print(c1.Cust_Details)
c1.dis_cust_check_balance()
c1.dis_deposit_amt()
c1.dis_withdraw_amt()
c1.dis_modify_pin()
c1.dis_modify_cust_data()
c1.dis_transfer_amt()
print(c1.transaction_details)
c1.dis_mini_stmt()