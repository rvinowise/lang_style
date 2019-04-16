#include "init_logging.hpp"

using namespace boost::log;


bool only_warnings(const attribute_value_set &set)
{
  return set["Severity"].extract<int>() > 0;
}

void init_logging()
{

}

void deinit_logging() {

}
