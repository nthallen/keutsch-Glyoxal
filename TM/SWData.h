/* SWData.h */
#ifndef SWDATA_H_INCLUDED
#define SWDATA_H_INCLUDED

typedef struct __attribute__((__packed__)) {
  unsigned char SWStat;
  unsigned char Flag;
} SWData_t;
extern SWData_t SWData;

#define SWS_PPS_IDLE 1
#define SWS_PPS_SYNC 2
#define SWS_TIMEWARP 254
#define SWS_SHUTDOWN 255

#endif
