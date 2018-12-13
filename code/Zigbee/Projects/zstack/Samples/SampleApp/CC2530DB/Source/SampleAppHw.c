#include "ZComDef.h"
#include "hal_mcu.h"
#include "hal_defs.h"

#include "SampleAppHw.h"

#define JUMPERIN_BIT  BV(2)  //P0.2
#define JUMPERIN_SEL  P0SEL
#define JUMPERIN_DIR  P0DIR
#define JUMPERIN      P0

#define JUMPEROUT_BIT BV(3)  //P0.3
#define JUMPEROUT_SEL P0SEL
#define JUMPEROUT_DIR P0DIR
#define JUMPEROUT     P0


uint8 readCoordinatorJumper( void )
{
  uint8 i,j;
  uint8 result;

  JUMPERIN_SEL  &= ~(JUMPERIN_BIT);
  JUMPERIN_DIR  &= ~(JUMPERIN_BIT);

  JUMPEROUT_SEL &= ~(JUMPEROUT_BIT);
  JUMPEROUT_DIR |= JUMPEROUT_BIT;

  // Start with output bit OFF
  JUMPEROUT &= ~(JUMPEROUT_BIT);

  for ( i = 0; i < 8; i++ )
  {
    for ( j = 0; j < 8; j++ )
    {
      // Burn time for input to see change
      result = JUMPERIN & JUMPERIN_BIT;
    }

    j = i & 0x01;
    if (((j == 0) && (result != 0)) ||
        ((j != 0) && (result != JUMPERIN_BIT)))
    {
      return ( FALSE );
    }

    // Toggle the output bit
    JUMPEROUT ^= JUMPEROUT_BIT;
  }

  return ( TRUE );
}

