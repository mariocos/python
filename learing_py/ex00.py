import requests




ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


response = requests.get('https://ipinfo.io/json')
data = response.json()

city = data.get('city', 'Unknown')
country = data.get('country', 'Unknown')

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], country)
ft_set = {"Hello", city}
ft_dict["Hello"] = "42" + city



print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)