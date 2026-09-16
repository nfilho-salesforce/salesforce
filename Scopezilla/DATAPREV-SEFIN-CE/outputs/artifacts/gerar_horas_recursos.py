#!/usr/bin/env python3
"""
Gera XLSX com horas por recurso, por semana, com taxas e fases
DATAPREV-SEFIN-CE v2.0 - ESCOPO BASE (sem ADD-ONs)
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import json

# Taxas diárias BRL (com impostos 75.35%)
TAXA_ARCHITECT_DIA = 7032.56
TAXA_DEVELOPER_DIA = 5725.28

# Converter para hora (8h/dia)
TAXA_ARCHITECT_HORA = TAXA_ARCHITECT_DIA / 8  # R$ 879,07/h
TAXA_DEVELOPER_HORA = TAXA_DEVELOPER_DIA / 8  # R$ 715,66/h

# Cores Salesforce
COLOR_BLUE = "0176D3"
COLOR_ORANGE = "FF9E2C"
COLOR_GREEN = "04844B"
COLOR_GRAY = "ECEBEA"
COLOR_RED = "EA001E"

# Estrutura do projeto (ESCOPO BASE - sem Phase 4 ADD-ON)
# 20 semanas cenário médio
PHASES = [
    {"phase": "Phase 0", "name": "Discovery Resolution", "weeks": [1, 2, 3]},
    {"phase": "Phase 1", "name": "Foundation & ORG Setup", "weeks": [4, 5, 6, 7]},
    {"phase": "Phase 2", "name": "Einstein Bot + API Integration", "weeks": [8, 9, 10, 11, 12, 13, 14, 15]},
    {"phase": "Phase 3", "name": "UX Research & Refinement", "weeks": [16, 17, 18, 19, 20]}
]

# Recursos e carga semanal por fase (horas/semana)
RESOURCES = [
    {
        "id": "R01",
        "name": "Technical Architect",
        "rate_class": "architect",
        "hours_by_phase": {
            "Phase 0": 20,  # Suporte arquitetural gap resolution
            "Phase 1": 40,  # Full-time architecture ownership
            "Phase 2": 30,  # Integration patterns design
            "Phase 3": 20   # UX accessibility consultoria
        }
    },
    {
        "id": "R02",
        "name": "Technical Consultant",
        "rate_class": "developer",
        "hours_by_phase": {
            "Phase 0": 0,   # Não ativo
            "Phase 1": 40,  # Build ORG + WhatsApp Channel
            "Phase 2": 40,  # Build Einstein Bot + APIs
            "Phase 3": 0    # Não ativo
        }
    },
    {
        "id": "R03",
        "name": "Technical Consultant (Security)",
        "rate_class": "developer",
        "hours_by_phase": {
            "Phase 0": 0,   # Não ativo
            "Phase 1": 30,  # Security baseline + profiles
            "Phase 2": 20,  # Named Credentials + data retention
            "Phase 3": 0    # Não ativo
        }
    },
    {
        "id": "R04",
        "name": "Experience Architect",
        "rate_class": "architect",
        "hours_by_phase": {
            "Phase 0": 0,   # Não ativo
            "Phase 1": 0,   # Não ativo
            "Phase 2": 0,   # Não ativo
            "Phase 3": 40   # Full-time UX research
        }
    },
    {
        "id": "R05",
        "name": "Technical Architect (Phase 0)",
        "rate_class": "architect",
        "hours_by_phase": {
            "Phase 0": 40,  # Full-time gap resolution orchestration
            "Phase 1": 0,   # Não ativo
            "Phase 2": 0,   # Não ativo
            "Phase 3": 0    # Não ativo
        }
    },
    {
        "id": "R06",
        "name": "Project Manager",
        "rate_class": "architect",  # PM usa taxa architect
        "hours_by_phase": {
            "Phase 0": 30,  # Coordenação gap resolution
            "Phase 1": 20,  # Delivery orchestration
            "Phase 2": 20,  # Dependency management
            "Phase 3": 15   # Stakeholder communication
        }
    }
]

def create_workbook():
    wb = openpyxl.Workbook()

    # Sheet 1: Horas por Semana
    ws1 = wb.active
    ws1.title = "Horas por Semana"
    create_hours_sheet(ws1)

    # Sheet 2: Resumo por Fase
    ws2 = wb.create_sheet("Resumo por Fase")
    create_summary_sheet(ws2)

    # Sheet 3: Resumo por Recurso
    ws3 = wb.create_sheet("Resumo por Recurso")
    create_resource_summary_sheet(ws3)

    # Sheet 4: Investimento Total
    ws4 = wb.create_sheet("Investimento Total")
    create_investment_sheet(ws4)

    return wb

def create_hours_sheet(ws):
    """Sheet 1: Horas por Semana detalhado"""

    # Headers
    ws['A1'] = "DATAPREV-SEFIN-CE v2.0 - HORAS POR SEMANA (ESCOPO BASE - SEM ADD-ONs)"
    ws['A1'].font = Font(size=14, bold=True, color="FFFFFF")
    ws['A1'].fill = PatternFill(start_color=COLOR_BLUE, end_color=COLOR_BLUE, fill_type="solid")
    ws.merge_cells('A1:I1')

    # Column headers
    headers = ["Semana", "Fase", "Recurso", "Papel", "Horas/Semana", "Taxa R$/Hora", "Custo Semana (R$)", "Custo Acumulado (R$)", "% Projeto"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col)
        cell.value = header
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color=COLOR_BLUE, end_color=COLOR_BLUE, fill_type="solid")
        cell.alignment = Alignment(horizontal='center', vertical='center')

    # Data rows
    row = 4
    cumulative_cost = 0
    total_hours = 0

    for phase in PHASES:
        phase_name = phase["phase"]
        phase_desc = phase["name"]

        for week in phase["weeks"]:
            for resource in RESOURCES:
                hours = resource["hours_by_phase"].get(phase_name, 0)
                if hours > 0:
                    rate_class = resource["rate_class"]
                    rate_hour = TAXA_ARCHITECT_HORA if rate_class == "architect" else TAXA_DEVELOPER_HORA
                    cost_week = hours * rate_hour
                    cumulative_cost += cost_week
                    total_hours += hours

                    ws.cell(row=row, column=1).value = week
                    ws.cell(row=row, column=2).value = f"{phase_name} - {phase_desc}"
                    ws.cell(row=row, column=3).value = resource["id"]
                    ws.cell(row=row, column=4).value = resource["name"]
                    ws.cell(row=row, column=5).value = hours
                    ws.cell(row=row, column=6).value = rate_hour
                    ws.cell(row=row, column=6).number_format = 'R$ #,##0.00'
                    ws.cell(row=row, column=7).value = cost_week
                    ws.cell(row=row, column=7).number_format = 'R$ #,##0.00'
                    ws.cell(row=row, column=8).value = cumulative_cost
                    ws.cell(row=row, column=8).number_format = 'R$ #,##0.00'
                    ws.cell(row=row, column=9).value = cumulative_cost / 4231269  # Percentual do ROM high
                    ws.cell(row=row, column=9).number_format = '0.0%'

                    # Color code by phase
                    phase_color = COLOR_ORANGE if phase_name == "Phase 0" else COLOR_GREEN if phase_name == "Phase 1" else COLOR_BLUE if phase_name == "Phase 2" else "9370DB"
                    ws.cell(row=row, column=2).fill = PatternFill(start_color=phase_color, end_color=phase_color, fill_type="solid")
                    ws.cell(row=row, column=2).font = Font(color="FFFFFF", bold=True)

                    row += 1

    # Total row
    ws.cell(row=row, column=1).value = "TOTAL"
    ws.cell(row=row, column=1).font = Font(bold=True, size=12)
    ws.cell(row=row, column=5).value = total_hours
    ws.cell(row=row, column=5).font = Font(bold=True, size=12)
    ws.cell(row=row, column=7).value = cumulative_cost
    ws.cell(row=row, column=7).font = Font(bold=True, size=12)
    ws.cell(row=row, column=7).number_format = 'R$ #,##0.00'

    # Adjust column widths
    ws.column_dimensions['A'].width = 10
    ws.column_dimensions['B'].width = 40
    ws.column_dimensions['C'].width = 10
    ws.column_dimensions['D'].width = 35
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 18
    ws.column_dimensions['H'].width = 20
    ws.column_dimensions['I'].width = 12

def create_summary_sheet(ws):
    """Sheet 2: Resumo por Fase"""

    ws['A1'] = "RESUMO POR FASE - ESCOPO BASE"
    ws['A1'].font = Font(size=14, bold=True, color="FFFFFF")
    ws['A1'].fill = PatternFill(start_color=COLOR_BLUE, end_color=COLOR_BLUE, fill_type="solid")
    ws.merge_cells('A1:F1')

    headers = ["Fase", "Descrição", "Semanas", "Total Horas", "Custo (R$)", "% Total"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col)
        cell.value = header
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color=COLOR_BLUE, end_color=COLOR_BLUE, fill_type="solid")
        cell.alignment = Alignment(horizontal='center')

    row = 4
    grand_total_hours = 0
    grand_total_cost = 0

    for phase in PHASES:
        phase_name = phase["phase"]
        phase_desc = phase["name"]
        num_weeks = len(phase["weeks"])

        phase_hours = 0
        phase_cost = 0

        for resource in RESOURCES:
            hours_per_week = resource["hours_by_phase"].get(phase_name, 0)
            rate_hour = TAXA_ARCHITECT_HORA if resource["rate_class"] == "architect" else TAXA_DEVELOPER_HORA
            phase_hours += hours_per_week * num_weeks
            phase_cost += hours_per_week * num_weeks * rate_hour

        grand_total_hours += phase_hours
        grand_total_cost += phase_cost

        ws.cell(row=row, column=1).value = phase_name
        ws.cell(row=row, column=2).value = phase_desc
        ws.cell(row=row, column=3).value = num_weeks
        ws.cell(row=row, column=4).value = phase_hours
        ws.cell(row=row, column=5).value = phase_cost
        ws.cell(row=row, column=5).number_format = 'R$ #,##0.00'
        ws.cell(row=row, column=6).value = phase_cost / 4231269
        ws.cell(row=row, column=6).number_format = '0.0%'

        row += 1

    # Total
    ws.cell(row=row, column=1).value = "TOTAL"
    ws.cell(row=row, column=1).font = Font(bold=True, size=12)
    ws.cell(row=row, column=3).value = 20
    ws.cell(row=row, column=3).font = Font(bold=True, size=12)
    ws.cell(row=row, column=4).value = grand_total_hours
    ws.cell(row=row, column=4).font = Font(bold=True, size=12)
    ws.cell(row=row, column=5).value = grand_total_cost
    ws.cell(row=row, column=5).font = Font(bold=True, size=12)
    ws.cell(row=row, column=5).number_format = 'R$ #,##0.00'

    ws.column_dimensions['A'].width = 12
    ws.column_dimensions['B'].width = 35
    ws.column_dimensions['C'].width = 12
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 18
    ws.column_dimensions['F'].width = 12

def create_resource_summary_sheet(ws):
    """Sheet 3: Resumo por Recurso"""

    ws['A1'] = "RESUMO POR RECURSO - ESCOPO BASE"
    ws['A1'].font = Font(size=14, bold=True, color="FFFFFF")
    ws['A1'].fill = PatternFill(start_color=COLOR_BLUE, end_color=COLOR_BLUE, fill_type="solid")
    ws.merge_cells('A1:G1')

    headers = ["ID", "Recurso", "Taxa R$/Hora", "Fases Ativas", "Total Horas", "Custo Total (R$)", "% Total"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col)
        cell.value = header
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color=COLOR_BLUE, end_color=COLOR_BLUE, fill_type="solid")
        cell.alignment = Alignment(horizontal='center')

    row = 4
    grand_total_hours = 0
    grand_total_cost = 0

    for resource in RESOURCES:
        rate_hour = TAXA_ARCHITECT_HORA if resource["rate_class"] == "architect" else TAXA_DEVELOPER_HORA

        resource_hours = 0
        active_phases = []

        for phase in PHASES:
            phase_name = phase["phase"]
            hours_per_week = resource["hours_by_phase"].get(phase_name, 0)
            if hours_per_week > 0:
                num_weeks = len(phase["weeks"])
                resource_hours += hours_per_week * num_weeks
                active_phases.append(phase_name)

        resource_cost = resource_hours * rate_hour
        grand_total_hours += resource_hours
        grand_total_cost += resource_cost

        ws.cell(row=row, column=1).value = resource["id"]
        ws.cell(row=row, column=2).value = resource["name"]
        ws.cell(row=row, column=3).value = rate_hour
        ws.cell(row=row, column=3).number_format = 'R$ #,##0.00'
        ws.cell(row=row, column=4).value = ", ".join(active_phases)
        ws.cell(row=row, column=5).value = resource_hours
        ws.cell(row=row, column=6).value = resource_cost
        ws.cell(row=row, column=6).number_format = 'R$ #,##0.00'
        ws.cell(row=row, column=7).value = resource_cost / 4231269
        ws.cell(row=row, column=7).number_format = '0.0%'

        row += 1

    # Total
    ws.cell(row=row, column=1).value = "TOTAL"
    ws.cell(row=row, column=1).font = Font(bold=True, size=12)
    ws.cell(row=row, column=5).value = grand_total_hours
    ws.cell(row=row, column=5).font = Font(bold=True, size=12)
    ws.cell(row=row, column=6).value = grand_total_cost
    ws.cell(row=row, column=6).font = Font(bold=True, size=12)
    ws.cell(row=row, column=6).number_format = 'R$ #,##0.00'

    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 35
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 25
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 18
    ws.column_dimensions['G'].width = 12

def create_investment_sheet(ws):
    """Sheet 4: Investimento Total"""

    ws['A1'] = "INVESTIMENTO TOTAL - ESCOPO BASE"
    ws['A1'].font = Font(size=14, bold=True, color="FFFFFF")
    ws['A1'].fill = PatternFill(start_color=COLOR_BLUE, end_color=COLOR_BLUE, fill_type="solid")
    ws.merge_cells('A1:B1')

    # Calculate totals
    total_hours = 0
    total_cost = 0

    for phase in PHASES:
        for resource in RESOURCES:
            hours_per_week = resource["hours_by_phase"].get(phase["phase"], 0)
            num_weeks = len(phase["weeks"])
            rate_hour = TAXA_ARCHITECT_HORA if resource["rate_class"] == "architect" else TAXA_DEVELOPER_HORA
            total_hours += hours_per_week * num_weeks
            total_cost += hours_per_week * num_weeks * rate_hour

    row = 3

    data = [
        ("Projeto", "DATAPREV-SEFIN-CE v2.0"),
        ("Escopo", "Service Cloud + Einstein Bot + WhatsApp (ESCOPO BASE - sem ADD-ONs)"),
        ("", ""),
        ("Timeline", "20 semanas (cenário médio)"),
        ("Total Horas", f"{total_hours:,.0f} horas"),
        ("", ""),
        ("Taxa Architect (R$/hora)", f"R$ {TAXA_ARCHITECT_HORA:,.2f}"),
        ("Taxa Developer (R$/hora)", f"R$ {TAXA_DEVELOPER_HORA:,.2f}"),
        ("", ""),
        ("INVESTIMENTO TOTAL", f"R$ {total_cost:,.2f}"),
        ("", ""),
        ("ROM Referência Low", "R$ 1.583.232,00"),
        ("ROM Referência High", "R$ 4.231.269,00"),
        ("Investimento Calculado", f"R$ {total_cost:,.2f}"),
        ("% do ROM High", f"{(total_cost / 4231269) * 100:.1f}%"),
        ("", ""),
        ("Observações", ""),
        ("", "Investimento calculado baseado em horas estimadas por fase"),
        ("", "ROM considera riscos, complexidade e margem de contingência"),
        ("", "ADD-ONs E07 (KB) e E08 (MC) não incluídos neste cálculo"),
        ("", "Licenças Salesforce não incluídas (cliente contrata diretamente)")
    ]

    for item, value in data:
        ws.cell(row=row, column=1).value = item
        ws.cell(row=row, column=2).value = value

        if item in ["INVESTIMENTO TOTAL", "Projeto"]:
            ws.cell(row=row, column=1).font = Font(bold=True, size=12, color="FFFFFF")
            ws.cell(row=row, column=1).fill = PatternFill(start_color=COLOR_GREEN, end_color=COLOR_GREEN, fill_type="solid")
            ws.cell(row=row, column=2).font = Font(bold=True, size=12)
        elif item in ["Timeline", "Total Horas"]:
            ws.cell(row=row, column=1).font = Font(bold=True)

        row += 1

    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 60

def main():
    print("Gerando XLSX com horas por recurso...")

    wb = create_workbook()
    output_path = 'DATAPREV_SEFIN_CE_Horas_Recursos.xlsx'
    wb.save(output_path)

    # Calculate summary
    total_hours = 0
    total_cost = 0

    for phase in PHASES:
        for resource in RESOURCES:
            hours_per_week = resource["hours_by_phase"].get(phase["phase"], 0)
            num_weeks = len(phase["weeks"])
            rate_hour = TAXA_ARCHITECT_HORA if resource["rate_class"] == "architect" else TAXA_DEVELOPER_HORA
            total_hours += hours_per_week * num_weeks
            total_cost += hours_per_week * num_weeks * rate_hour

    print(f"\n✅ XLSX gerado: {output_path}")
    print(f"\n📊 RESUMO:")
    print(f"   Timeline: 20 semanas (4 fases)")
    print(f"   Total Horas: {total_hours:,.0f} horas")
    print(f"   Investimento: R$ {total_cost:,.2f}")
    print(f"   % ROM High: {(total_cost / 4231269) * 100:.1f}%")
    print(f"\n📋 4 Sheets:")
    print(f"   1. Horas por Semana (detalhe semana a semana)")
    print(f"   2. Resumo por Fase")
    print(f"   3. Resumo por Recurso")
    print(f"   4. Investimento Total")

if __name__ == '__main__':
    main()
