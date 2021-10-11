from collections import deque;
graph = {};
graph["you"] = ["alice", "bob", "claire"];
graph["bob"] = ["anuj", "peggy"];
graph["alice"] = ["peggy"];
graph["claire"] = ["thom", "jhonny"];
graph["anuj"] = [];
graph["peggy"] = [];
graph["thom"] = [];
graph["jhonny"] = [];

def person_is_seller(name):
    return name[-1] == 'm';

def search(name):
    search_queue = deque();
    search_queue += graph[name];
    searched = [];
    while search_queue:
        person = search_queue.popleft();
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango Seller!!");
                return True;
            else:
                search_queue += graph[person];
                searched.append(person);
    return False;
if __name__ == "__main__":
    search("you");