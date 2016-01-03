#include "luck.hpp"
#include <boost/python.hpp>
#include <numeric>
#include <cctype>
#include <algorithm>


LUCK_DLL( bool isLucky(std::string str) )
{
    int sum = 0;
        std::for_each(str.begin(), str.end(),[&](int c){if(isdigit(c)) sum+= c-'0';});
    return 0 == (sum % 7);
}




BOOST_PYTHON_MODULE(luck)
{
    boost::python::def( "isLucky", isLucky );
}
