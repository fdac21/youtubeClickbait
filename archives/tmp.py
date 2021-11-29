def list_num_to_num(nums)-> int:
    ret = ''

    idk = nums.replace(' ', '')
    idk = idk.replace('[', '')
    idk = idk.replace(']', '')
    idk = idk.split(',')
    
    
    for x, entry in enumerate(idk):
        
        st = str(entry)
        tmst = ''
        #tmst += ('0' * (8 - (len(st))))
        ret += tmst+st
        if x == 5:
            break
    
    return ret


def list_num_to_num_wlen(nums)-> int:
    ret = ''
    for entry in nums:
        st = str(entry)
        #print(str(len(st))+st)
        ret += str(len(st))+st

    return ret

#print(list_num_to_num_wlen([10, 20, 3, 40]))