/* SPDX-License-Identifier: GPL-2.0 */
#ifndef _UAPI_AURA_PCI_DEV_I2C_H
#define _UAPI_AURA_PCI_DEV_I2C_H

#include <linux/pci.h>
#include "asic/asic-types.h"

/*
    AMD devices require an i2c adapter to be created,
    NVIDIA devices already have the adapter loaded.
 */
static const struct pci_device_id pciidlist[] = {
    {0x1002, 0x67df, PCI_ANY_ID, PCI_ANY_ID, 0, 0, CHIP_POLARIS10}, //470-590
    {0x1002, 0x67c7, PCI_ANY_ID, PCI_ANY_ID, 0, 0, CHIP_POLARIS10}, //wx5100
    {0x1002, 0x6fdf, PCI_ANY_ID, PCI_ANY_ID, 0, 0, CHIP_POLARIS10}, //580 2048Sp/590GME
    {0x1002, 0x67FF, PCI_ANY_ID, PCI_ANY_ID, 0, 0, CHIP_POLARIS11},     // RX560
    {0x1002, 0x687F, PCI_ANY_ID, PCI_ANY_ID, 0, 0, CHIP_VEGA10},        // Vega
    // {0x1002, 0x731f, PCI_ANY_ID, PCI_ANY_ID, 0, 0, CHIP_NAVI10},     // RX5700XT
    {0, 0, 0},
};

#endif
