test_case = int(input())
for tc in range(test_case):
    F = int(input())
    friend_dict = dict()
    
    for friend in range(F):
        name1, name2 = input().split()
        
        
        def dict_append(name):
            key_list = []
            value_list = []
            for k, v in friend_dict.items():
                if name in v:
                    key_list.append(k)
                    value_list.extend(v)
            value_set = set(value_list)

            return key_list, value_set
        
        
        friend_dict_values = []
        for v in friend_dict.values():
            friend_dict_values.extend(v)
        
        if name1 not in friend_dict_values:
            # 완전 처음 친구 관계인 경우
            if name2 not in friend_dict_values:
                friend_dict.setdefault(friend, [name1, name2])
                print(2)
            
            # name2 만 기존에 관계가 있는 경우
            else:
                key_list, value_set = dict_append(name2)
                value_set.add(name1)
                # 두 친구관계를 안 합쳐도 되는 경우
                if len(key_list) == 1:
                    friend_dict[key_list[0]] = value_set
                    print(len(value_set))
                
                else:
                    first = True
                    for key in key_list():
                        if first == True:
                            friend_dict[key] = value_set
                            first = False
                        else:
                            del friend_dict[key]
                    print(len(value_set))
        
        else:
            # name1 만 기존의 관계가 있는 경우
            if name2 not in friend_dict_values: 
                key_list, value_set = dict_append(name1)
                value_set.add(name2)
                # 두 친구관계를 안합쳐도 되는 경우
                if len(key_list) == 1:
                    friend_dict[key_list[0]] = value_set
                    print(len(value_set))
                
                else:
                    first = True
                    for key in key_list():
                        if first == True:
                            friend_dict[key] = value_set
                            first = False
                        else:
                            del friend_dict[key]
                    print(len(value_set))
                            
            # name1, name2 다 있지만 둘이 다른 친구관계인 경우!
            else:
                key_list_1, value_set_1 = dict_append(name1)
                key_list_2, value_set_2 = dict_append(name2)
                
                key_list = key_list_1 + key_list_2
                value_list = list(value_set_1) + list(value_set_2)
                value_set = set(value_list)
                
                first = True
                for key in key_list:
                    if first == True:
                        friend_dict[key] = value_set
                        first = False
                    else:
                        del friend_dict[key]
                print(len(value_set))
