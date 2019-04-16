#pragma once

#include <boost/log/trivial.hpp>
#include <boost/log/common.hpp>
#include <boost/log/sinks.hpp>
#include <boost/log/sources/severity_logger.hpp>
#include <boost/core/null_deleter.hpp>
#include <boost/shared_ptr.hpp>
#include <iostream>


// a part of the library init function
void init_logging();
void deinit_logging();

#define LOG(param) BOOST_LOG_TRIVIAL(param)
