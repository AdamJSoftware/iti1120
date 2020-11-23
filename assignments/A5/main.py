a = [(0,1),(0,2),(0,3), (1,4), (1,6), (1,7), (1,9), (2,3), (2,6), (2,8), (2,9), (3,8), (3,9), (4,6), (4,7), (4,8), (5,9), (6,8), (7,8)]


def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def create_initial_array(file):
    arr = []
    index = 0
    for item in file:
        if index != 0 and item != '':
            item = item.split(' ')
            print(item)
            item1 = item[0]
            item2 = item[1]
            arr.append((int(item1), int(item2)))
        index +=1
    return arr


def create_network(filename):

    print(filename)
    c = open(file_name)
    e = c.read()
    e = e.split('\n')
    print(e)
    a = create_initial_array(e)
    available_users = []
    for item in a:
        for user in item:
            if(not(user in available_users)):
                available_users.append(user)
    print(f"avialable users: {available_users}")
    user_relationships = []
    available_users.sort()
    for user in available_users:
        print(user)
        relationships = []
        for relationship in a:
            if user in relationship:
                for person in relationship:
                    if person != user and not(person in relationships):
                        relationships.append(person)
        relationships.sort()
        user_relationships.append((user, relationships))
    print(user_relationships)
    c.close()
    return user_relationships


def getCommonFriends(user1, user2, network):
    common_friends = []
    user1 = network[user1][1]
    user2 = network[user2][1]
    for friend in user1:
        if friend in user2:
            common_friends.append(friend)
    return common_friends

def recommended(user, network):
    users_friends = network[user][1]
    common_friends_id = []
    common_friends_amount = []
    for friend in users_friends:
        friends_friends= network[friend][1]
        for common_friend in friends_friends:
            if not(common_friend in users_friends):
                if common_friend in common_friends_id:
                    position = common_friends_id.index(common_friend)
                    common_friends_amount[position] = common_friends_amount[position] + 1 
                else:
                    common_friends_id.append(common_friend)
                    common_friends_amount.append(1)
    if(len(common_friends_id) == 0):
        return None
    largest_connections = max(common_friends_amount)
    amount_largest_connections = common_friends_amount.count(largest_connections)
    if(amount_largest_connections == 1):
        return common_friends_id[common_friends_amount.index(largest_connections)]
    else:
        user_ids_list = []
        index = 0
        for item in amount_largest_connections:
            if item == largest_connections:
                user_ids_list.append(common_friends_id[index])
            index +=1
        user_ids_list.sort()
        return user_ids_list[-1]
    
def k_or_more_friends(network, k):
    ammount_of_users = 0
    for item in network:
        if k <= len(item[1]):
            ammount_of_users += 1
    return ammount_of_users

def maximum_num_friends(network):
    max_friends_amount = 0
    for item in network:
        if max_friends_amount < len(item[1]):
            max_friends_amount = len(item[1])
    return max_friends_amount

def people_with_most_friends(network):
    max_friends_amount = maximum_num_friends(network)
    max_friends=[]
    for item in network:
        if max_friends_amount == len(item[1]):
            max_friends.append(item[0])
    # YOUR CODE GOES HERE
    return max_friends

def average_num_friends(network):
    total_friends_amount = 0
    for item in network:
        total_friends_amount += len(item[1])
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    return total_friends_amount / len(network)

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    for item in network:
        if(len(item[1]) == len(network) - 1):
            return True
    return False

if __name__ == "__main__":
    file_name=get_file_name()
    net=create_network(file_name)
    print(getCommonFriends(3,1,net))
