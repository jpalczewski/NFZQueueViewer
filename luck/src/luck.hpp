#ifndef LUCK_H_
#define LUCK_H_
#include <boost/python.hpp>
#include <string>

#if defined(_MSC_VER) && (_MSC_VER >= 1400)
//msvc disable warnings for sheduler_ and history_ member
#pragma warning(disable:4251)
#endif


#ifdef LUCK_EXPORTS
/** Workaround for Windows DLL library exports */
#define LUCK_DLL(X) __declspec(dllexport)X
#else
/** Workaround for Unix Shared Library exports */
#define LUCK_DLL(X) X
#endif


LUCK_DLL( bool isLucky(std::string str) );



#endif
