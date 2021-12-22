'''
Imagine you have a call center with three levels of employees: fresher, technical lead (TL), product manager (PM).
There can be multiple employees, but only one TL or PM. An incoming telephone call must be allocated to a fresher who is free.
If a fresher can’t handle the call, he or she must escalate the call to technical lead. If the TL is not free or not able to handle it,
then the call should be escalated to PM. Design the classes and data structures for this problem. Implement a method getCallHandler().
'''

from collections import deque
class Employee():
    _types = {"Fresher": 1, "TL": 2, "PM": 3}

    def __init__(self, emp_id, emp_name, emp_type):
        self.employee_id = emp_id
        self.employee_name = emp_name
        self.employee_type = Employee._types[emp_type]
        self.on_call = False

        #self.call_handler = Call_Handler()

    ''' Assign the call to an employee'''
    def assign_call(self, call):
        random_escalation = random.randrange(0,10)
        if random_escalation == 1:
            self.escalate(call)
            return 0, call
        else:
            self.on_call = True
            call.handled_by = self
            return 1, call
    '''
        Check if employee is free or on call
    '''
    def is_free(self):
        return self.on_call is False

    def call_over(self):
        self.on_call = False
        #return self.employee_id

    def escalate(self, call):
        self.on_call = False
        call.call_rank = call.call_rank + 1
        #self.call_handler.get_call_handler(call)
        return call #self.employee_id

class Call():
    def __init__(self, number, rank, handled_by):
        self.call_number = number
        self.call_rank = rank
        self.handled_by = handled_by


class Call_Center():
    def __init__(self, no_of_emp):
        self.call_center_id = 1
        self.number_of_employees = no_of_emp
        self.number_of_levels = 3

    '''
    def assign_call_higher(self, call):
        """
        :param call:
        """
        if self.tl.is_free():
            self.tl.assign_call()
            if self.tl.escalate():
                self.tl.
        else:
            if self.pm.is_free():
                self.pm.assign_call()
            else:
                self.pending_calls.append(call)
    '''

class Call_Handler():
    def __init__(self, call_center):
        self.free_employees = []
        self.pending_calls = deque()
        self.call_center = call_center
        self.busy_employees = [deque() for index in range(self.call_center.number_of_levels)]
        #Not Required for current requirement

        initial_employee = deque()
        for index in range(self.call_center.number_of_employees):
            emp = Employee(index, "R" + index, "Fresher")
            initial_employee.append(emp)
            # self.free_employees[index] = emp

        self.free_employees.append(initial_employee)

        initial_employee = deque()
        emp = Employee(self.number_of_employees, "R" + self.number_of_employees, "TL")  # self.tl
        initial_employee.append(emp)
        self.free_employees.append(initial_employee)

        initial_employee = deque()
        emp = Employee(self.number_of_employees + 1, "R" + self.number_of_employees + 1, "PM")  # self.pm
        initial_employee.append(emp)
        self.free_employees.append(initial_employee)

    def assign_call(self, call):
        #Check if any fresher is free
        for call_rank in (call.call_rank, self.call_center.number_of_levels+1):
            free_emp_list = self.free_employees[call_rank-1]
            if len(self.free_emp_list) > 0:
                emp = self.free_employees.popleft()
                assigned_yn, returned_call = emp.assign_call(call)
                if assigned_yn == 1:
                    self.busy_employees[call.call_rank - 1].append(emp)
                    return
                else:
                    self.assign_call(returned_call)
            else:
                self.pending_calls.append(call)

    def get_next_call(self):
        return self.pending_calls.popleft()

    def call_over(self, call):
        call.handled_by.call_over()
        self.free_employees[call.call_rank - 1].append(call.handled_by)
        self.busy_employees[call.call_rank - 1].remove(call.handled_by)
        '''
        current_list = self.free_employees[call.call_rank-1]
        current_list.append(call.handled_by)
        self.free_employees[call.call_rank - 1] = current_list
        '''

import random
if __name__ == '__main__':
    call_center = Call_Center(50)
    call_handler = Call_Handler(call_center)

    number_of_calls = random.randrange(1, 50)
    for index in range(number_of_calls):
        call = Call(index, 1, None)
        call_handler.assign_call(call)