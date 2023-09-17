from collections import UserDict

def input_error(func):
    def Inner(*args):
        try:
            res = func(*args)
        except KeyError:
            print("Use valid contact!")
            exit
        except ValueError:
            print("Write valid phone number")
            exit
        else:
            return res
    return Inner

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        int(value)
        if len(value) == 10:
            self.value = value
        else:
            raise ValueError

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    @input_error
    def add_phone(self, phone):
        int(phone)
        self.phone = Phone(phone)
        self.phones.append(self.phone)
    
    # @input_error    
    def edit_phone(self, old_phone, new_phone):
        new_list = [p.value for p in self.phones] 
        old_phone_indx = new_list.index(old_phone)
        new_list.remove(old_phone)
        sel_old_phone = self.phones.pop(old_phone_indx)
        self.phone = Phone(new_phone)
        self.phones.insert(old_phone_indx, self.phone)
    
    @input_error    
    def find_phone(self, phone):
        new_list = [p.value for p in self.phones]
        p_indx = new_list.index(phone)
        return self.phones[p_indx]
    
    @input_error        
    def remove_phone(self, phone):
        new_list = [p.value for p in self.phones] 
        phone_indx = new_list.index(phone)
        phone_del = self.phones.pop(phone_indx)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    @input_error    
    def find(self, name):
        for k in self.data.keys():
            if k == name:
                return self.data[k]
        print("There is no such contct in the address book")

    @input_error
    def delete(self, name):
        del_dict = self.data.pop(name)